import requests
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

# Initialize Vision Transformer pipeline (background loaded so server binds port immediately)
processor = None
model = None
model_loading = False
model_error = None
torch_module = None

def load_vit_model():
    global processor, model, model_loading, model_error, torch_module
    if model is not None or model_loading:
        return
    model_loading = True
    try:
        import torch
        from transformers import AutoImageProcessor, AutoModelForImageClassification
        torch_module = torch
        torch_module.set_num_threads(min(4, os.cpu_count() or 4))

        model_source = LOCAL_MODEL_DIR if os.path.exists(LOCAL_WEIGHTS) else HF_MODEL_ID
        print(f"[Ksetrin] Background loading Vision Transformer (ViT-Base-Patch16-224) from {model_source}...")
        t_start = time.time()
        processor = AutoImageProcessor.from_pretrained(model_source)
        model = AutoModelForImageClassification.from_pretrained(model_source)
        model.eval()

        # Warm-up pass to eliminate cold-start latency on subsequent requests
        try:
            with torch_module.inference_mode():
                dummy_input = torch_module.zeros((1, 3, 224, 224))
                _ = model(dummy_input)
        except Exception:
            pass

        print(f"[Ksetrin] Vision Transformer ready in {time.time() - t_start:.2f}s (98.97% accuracy, warmed up)")
        model_loading = False
    except Exception as e:
        model_error = str(e)
        model_loading = False
        print(f"[Ksetrin] Vision Transformer background load notice: {e}")

app = FastAPI(title="Ksetrin Crop Disease Detection API", version="3.0.0")

@app.on_event("startup")
async def startup_event():
    print("[Ksetrin] Fast inference routed to Hugging Face Space (https://ruougishiki-cropdiseasedetection.hf.space)")
    key_status = f"{GROQ_API_KEY[:8]}..." if GROQ_API_KEY else "NOT SET"
    print(f"[Ksetrin] Groq API key status: {key_status}")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HF_INFERENCE_URL = "https://ruougishiki-cropdiseasedetection.hf.space/api/predict"

def run_model_inference(image: Image.Image):
    """Execute Vision Transformer inference via high-speed Hugging Face Space (2 vCPU · 16 GB RAM)."""
    if image.mode != "RGB":
        image = image.convert("RGB")

    if image.width > 384 or image.height > 384:
        image.thumbnail((384, 384), Image.Resampling.BILINEAR)

    buf = io.BytesIO()
    image.save(buf, format="JPEG", quality=90)
    buf.seek(0)

    try:
        res = requests.post(
            HF_INFERENCE_URL,
            files={"file": ("leaf.jpg", buf, "image/jpeg")},
            timeout=25
        )
        if res.status_code == 200:
            return res.json()
        raise HTTPException(status_code=res.status_code, detail=f"Inference error from Hugging Face Space: {res.text}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Inference gateway error: {str(e)}")

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
    except HTTPException:
        raise
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
    except HTTPException:
        raise
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
    """Return list of all 38 recognized crop disease classes with complete agronomic profiles."""
    classes_list = []
    for cls in CLASS_NAMES:
        info = get_disease_info(cls)
        classes_list.append({
            "id": cls,
            "crop": info['crop'],
            "condition": info['condition'],
            "is_healthy": info['is_healthy'],
            "severity": info.get('severity', 'Standard'),
            "pathogen": info.get('pathogen', 'N/A'),
            "description": info.get('description', ''),
            "symptoms": info.get('symptoms', []),
            "organic_treatment": info.get('organic_treatment', []),
            "chemical_treatment": info.get('chemical_treatment', []),
            "prevention": info.get('prevention', [])
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
        "platform": "Ksetrin Smart Agriculture Studio"
    }

@app.get("/ping")
async def ping():
    """Ultra-lightweight keep-alive endpoint to prevent Render free-tier cold starts."""
    return {"pong": True}

class AuthRequest(BaseModel):
    email: str
    password: Optional[str] = None
    name: Optional[str] = None

class ChatRequest(BaseModel):
    message: str
    user_name: Optional[str] = "Farmer"
    user_purpose: Optional[str] = "Detection"
    context: Optional[str] = None
    diagnosis: Optional[dict] = None

def _get_groq_key():
    key = os.environ.get("GROQ_API_KEY")
    if key:
        return key.strip()
    env_file = os.path.join(BASE_DIR, ".env")
    if os.path.exists(env_file):
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("GROQ_API_KEY="):
                        return line.split("=", 1)[1].strip().strip('"').strip("'")
        except Exception:
            pass
    return ""

GROQ_API_KEY = _get_groq_key()

@app.post("/api/chat")
async def chat_with_bot(req: ChatRequest):
    """Chat endpoint powered by Groq LLM API with active leaf personalization."""
    import urllib.request
    import urllib.error
    import json

    
    user_name = req.user_name or "Farmer"
    user_purpose = req.user_purpose or "Crop Health & Disease Management"

    system_prompt = (
        f"You are Ksetrin AI, an intelligent agronomic and crop disease specialist. "
        f"You are assisting {user_name} ({user_purpose}). "
        "Provide direct, scientifically sound, and field-actionable agricultural advice. "
        "Structure answers clearly with: "
        "1) Diagnosis / Cause summary, "
        "2) Immediate Action & Treatment (certified organic and chemical options with exact application rates/dosages), "
        "3) Preventative Field Measures. "
        "Keep answers concise, direct, factual, and strictly under 180 words. Do not use emojis."
    )

    if req.diagnosis:
        d = req.diagnosis
        crop = d.get('crop', '')
        cond = d.get('condition', '')
        conf = d.get('confidence', '')
        sev = d.get('severity', '')
        pathogen = d.get('pathogen', '')
        desc = d.get('description', '')
        org = d.get('organic_treatment', [])
        chem = d.get('chemical_treatment', [])
        prev = d.get('prevention', [])
        sym = d.get('symptoms', [])

        system_prompt += (
            f"\n\nCURRENT LEAF UNDER ACTIVE INVESTIGATION:\n"
            f"- Crop: {crop}\n"
            f"- Condition: {cond} (Confidence: {conf}%)\n"
            f"- Severity: {sev}\n"
            f"- Pathogen: {pathogen}\n"
            f"- Clinical Description: {desc}\n"
            f"- Symptoms: {'; '.join(sym) if isinstance(sym, list) else sym}\n"
            f"- Certified Organic Treatment: {'; '.join(org) if isinstance(org, list) else org}\n"
            f"- Chemical Treatment: {'; '.join(chem) if isinstance(chem, list) else chem}\n"
            f"- Field Prevention: {'; '.join(prev) if isinstance(prev, list) else prev}\n"
            f"\nThe user is specifically asking questions regarding THIS active leaf diagnosis. "
            f"Tailor all agronomic advice, dosages, timing, and explanations directly to this leaf."
        )
    elif req.context:
        system_prompt += f" Current leaf diagnosis context: {req.context}."

    # Models confirmed active and supported on this Groq key
    candidate_models = ["qwen/qwen3.8-27b", "openai/gpt-oss-120b"]
    last_error = "Unknown error"

    for model in candidate_models:
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": req.message}
            ],
            "temperature": 0.2,
            "max_tokens": 450
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
                if reply and reply.strip():
                    return {"success": True, "reply": reply.strip()}
        except urllib.error.HTTPError as e:
            try:
                err_body = e.read().decode("utf-8")
            except Exception:
                err_body = str(e)
            print(f"[Ksetrin] Groq API {model} HTTP {e.code}: {err_body}")
            last_error = f"HTTP {e.code}: {err_body[:200]}"
            continue
        except Exception as e:
            print(f"[Ksetrin] Groq API {model} error: {e}")
            last_error = str(e)
            continue

    return {"success": False, "reply": f"AI service temporarily unavailable: {last_error}"}

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
