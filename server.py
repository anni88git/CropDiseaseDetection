import os
import time
import io
import base64
import numpy as np
from PIL import Image
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List

import json
from disease_info import get_disease_info, DISEASE_DB

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
SAMPLES_DIR = os.path.join(STATIC_DIR, 'samples')

# Vision Transformer Configuration
HF_MODEL_ID = "RuougiShiki/crop-disease-vit"
LOCAL_MODEL_DIR = os.path.join(BASE_DIR, 'best_vit_plant_model')
LOCAL_WEIGHTS = os.path.join(LOCAL_MODEL_DIR, 'model.safetensors')
LOCAL_CLASSES = os.path.join(LOCAL_MODEL_DIR, 'classes.json')

# Load 38 disease class definitions
if os.path.exists(LOCAL_CLASSES):
    with open(LOCAL_CLASSES, 'r', encoding='utf-8') as f:
        CLASS_NAMES = json.load(f)
else:
    CLASS_NAMES = [
        'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
        'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
        'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
        'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
        'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
        'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
        'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
        'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
        'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
        'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
        'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
        'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
        'Tomato___healthy'
    ]

# Initialize Vision Transformer pipeline
processor = None
model = None
torch = None

try:
    import torch
    from transformers import AutoImageProcessor, AutoModelForImageClassification
    
    model_source = LOCAL_MODEL_DIR if os.path.exists(LOCAL_WEIGHTS) else HF_MODEL_ID
    print(f"[Ksetrin] Initializing Vision Transformer (ViT-Base-Patch16-224) from {model_source}...")
    t_start = time.time()
    processor = AutoImageProcessor.from_pretrained(model_source)
    model = AutoModelForImageClassification.from_pretrained(model_source)
    model.eval()
    print(f"[Ksetrin] Vision Transformer ready in {time.time() - t_start:.2f}s (98.97% accuracy)")
except Exception as e:
    print(f"[Ksetrin] Vision Transformer will initialize upon environment startup: {e}")

app = FastAPI(title="Kṣetrin Crop Disease Detection API", version="3.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def run_model_inference(image: Image.Image):
    """Execute Vision Transformer (ViT-Base-Patch16-224) inference."""
    if model is None or processor is None:
        raise HTTPException(
            status_code=503, 
            detail="Vision Transformer is downloading or PyTorch/transformers are not yet installed in local environment."
        )
    
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    t0 = time.time()
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)[0]

    top5_probs, top5_indices = torch.topk(probabilities, 5)
    latency_ms = round((time.time() - t0) * 1000, 1)

    best_idx = int(top5_indices[0].item())
    best_class = model.config.id2label[best_idx] if hasattr(model.config, 'id2label') and best_idx in model.config.id2label else CLASS_NAMES[best_idx]
    confidence = float(top5_probs[0].item() * 100.0)

    top5 = []
    for prob, idx in zip(top5_probs, top5_indices):
        c_idx = int(idx.item())
        cls_name = model.config.id2label[c_idx] if hasattr(model.config, 'id2label') and c_idx in model.config.id2label else CLASS_NAMES[c_idx]
        cls_info = get_disease_info(cls_name)
        top5.append({
            "class_name": cls_name,
            "crop": cls_info['crop'],
            "condition": cls_info['condition'],
            "confidence": round(float(prob.item() * 100.0), 2),
            "is_healthy": cls_info['is_healthy']
        })

    disease_data = get_disease_info(best_class)
    is_unknown = confidence < 60.0

    return {
        "success": True,
        "predicted_class": best_class,
        "crop": disease_data['crop'],
        "condition": disease_data['condition'],
        "is_healthy": disease_data['is_healthy'],
        "confidence": round(confidence, 2),
        "confidence_level": "High" if confidence >= 85 else ("Moderate" if confidence >= 65 else "Low"),
        "is_unknown": is_unknown,
        "severity": disease_data['severity'],
        "pathogen": disease_data['pathogen'],
        "description": disease_data['description'],
        "symptoms": disease_data['symptoms'],
        "organic_treatment": disease_data['organic_treatment'],
        "chemical_treatment": disease_data['chemical_treatment'],
        "prevention": disease_data['prevention'],
        "top5": top5,
        "telemetry": {
            "latency_ms": latency_ms,
            "input_resolution": f"{image.width}x{image.height}",
            "model_architecture": "MobileNetV2 (Fine-Tuned Transfer Learning)",
            "classes_evaluated": len(CLASS_NAMES)
        }
    }

class Base64PredictRequest(BaseModel):
    image_base64: Optional[str] = None
    sample_name: Optional[str] = None

@app.post("/api/predict")
async def predict_file(file: UploadFile = File(...)):
    """Analyze uploaded leaf image file."""
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        return run_model_inference(image)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Image processing error: {str(e)}")

@app.post("/api/predict/json")
async def predict_json(req: Base64PredictRequest):
    """Analyze image via base64 or sample image name."""
    try:
        if req.sample_name:
            # Load from static/samples
            clean_name = os.path.basename(req.sample_name)
            sample_path = os.path.join(SAMPLES_DIR, clean_name)
            if not os.path.exists(sample_path):
                raise HTTPException(status_code=404, detail="Sample image not found.")
            image = Image.open(sample_path)
            return run_model_inference(image)
        elif req.image_base64:
            # Handle data:image/png;base64,... header if present
            b64_str = req.image_base64
            if "," in b64_str:
                b64_str = b64_str.split(",", 1)[1]
            data = base64.b64decode(b64_str)
            image = Image.open(io.BytesIO(data))
            return run_model_inference(image)
        else:
            raise HTTPException(status_code=400, detail="Either image_base64 or sample_name is required.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Inference error: {str(e)}")

@app.get("/api/samples")
async def get_samples():
    """Return available sample test images for instant testing."""
    samples = []
    if os.path.exists(SAMPLES_DIR):
        for f in sorted(os.listdir(SAMPLES_DIR)):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                # Create friendly label
                label = f.rsplit('.', 1)[0].replace('_', ' ').replace('  ', ' ')
                samples.append({
                    "filename": f,
                    "title": label,
                    "url": f"/static/samples/{f}"
                })
    return {"samples": samples}

@app.get("/api/classes")
async def get_classes():
    """Return list of all 38 recognized crop disease classes."""
    classes_list = []
    for cls in CLASS_NAMES:
        info = get_disease_info(cls)
        classes_list.append({
            "id": cls,
            "crop": info['crop'],
            "condition": info['condition'],
            "is_healthy": info['is_healthy']
        })
    return {"classes": classes_list, "total": len(classes_list)}

@app.get("/api/health")
async def health_check():
    """Return API and model health status."""
    return {
        "status": "online",
        "model_loaded": model is not None,
        "model_architecture": "Vision Transformer (ViT-Base-Patch16-224)",
        "model_accuracy": "98.97%",
        "classes_count": len(CLASS_NAMES),
        "platform": "Kṣetrin Smart Agriculture Studio"
    }

class AuthRequest(BaseModel):
    email: str
    password: Optional[str] = None
    name: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    user_name: Optional[str] = "Farmer"
    user_purpose: Optional[str] = "Detection"
    context: Optional[str] = None

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

@app.post("/api/chat")
async def chat_with_bot(req: ChatRequest):
    """Chat endpoint powered by Groq LLM API."""
    import urllib.request
    import json
    
    system_prompt = (
        f"You are Ksetrin AI, an intelligent agronomic and crop disease specialist. "
        f"You are assisting {req.user_name}, whose primary purpose is {req.user_purpose}. "
        "Provide direct, concise, and scientifically accurate agricultural advice. "
        "Do not use emojis in your response. Keep answers concise, factual, and helpful."
    )
    if req.context:
        system_prompt += f" Current leaf diagnosis context: {req.context}."

    payload = {
        "model": "qwen/qwen3.8-27b",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": req.message}
        ],
        "temperature": 0.6,
        "max_tokens": 400
    }

    try:
        url_req = urllib.request.Request(
            "https://api.groq.com/openai/v1/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0"
            }
        )
        with urllib.request.urlopen(url_req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            reply = data["choices"][0]["message"]["content"]
            return {"success": True, "reply": reply}
    except Exception as e:
        return {"success": False, "reply": f"AI service temporarily unavailable: {str(e)}"}

# Mount images and samples directly so relative asset paths work from both root and subpaths
images_path = os.path.join(STATIC_DIR, "images")
if os.path.exists(images_path):
    app.mount("/images", StaticFiles(directory=images_path), name="images")

samples_path = os.path.join(STATIC_DIR, "samples")
if os.path.exists(samples_path):
    app.mount("/samples", StaticFiles(directory=samples_path), name="samples")

# Serve static directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

NO_CACHE_HEADERS = {
    "Cache-Control": "no-cache, no-store, must-revalidate",
    "Pragma": "no-cache",
    "Expires": "0"
}

@app.get("/")
async def root():
    """Redirect to login or serve login page."""
    login_path = os.path.join(STATIC_DIR, "login.html")
    if os.path.exists(login_path):
        return FileResponse(login_path, headers=NO_CACHE_HEADERS)
    return {"message": "Ksetrin Crop Disease Detection System"}

@app.get("/login.html")
async def get_login_page():
    return FileResponse(os.path.join(STATIC_DIR, "login.html"), headers=NO_CACHE_HEADERS)

@app.get("/index.html")
async def get_index_page():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), headers=NO_CACHE_HEADERS)

@app.get("/app")
async def get_app_page():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"), headers=NO_CACHE_HEADERS)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=False)
