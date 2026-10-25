import os
import json
import streamlit as st
import torch
import numpy as np
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

# Page Configuration
st.set_page_config(
    page_title="AI Crop Disease Detector",
    page_icon="🌿",
    layout="wide"
)

# Hugging Face Model Repository
HF_MODEL_ID = "RuougiShiki/crop-disease-vit"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL_MODEL_DIR = os.path.join(BASE_DIR, 'best_vit_plant_model')
LOCAL_WEIGHTS = os.path.join(LOCAL_MODEL_DIR, 'model.safetensors')
LOCAL_CLASSES = os.path.join(LOCAL_MODEL_DIR, 'classes.json')

# Cache model and processor for lightning fast inference
@st.cache_resource
def load_vit_pipeline():
    try:
        # Check if full model is present locally (e.g. on your local machine or in Docker)
        if os.path.exists(LOCAL_WEIGHTS):
            model_source = LOCAL_MODEL_DIR
            status_source = "Local weights"
        else:
            # Fallback: seamlessly fetch and cache directly from Hugging Face Hub
            model_source = HF_MODEL_ID
            status_source = f"Hugging Face Hub ({HF_MODEL_ID})"

        with st.spinner(f"Loading Vision Transformer from {status_source}..."):
            processor = AutoImageProcessor.from_pretrained(model_source)
            model = AutoModelForImageClassification.from_pretrained(model_source)
            model.eval()

        # Load classes from local classes.json or from Hugging Face config id2label
        if os.path.exists(LOCAL_CLASSES):
            with open(LOCAL_CLASSES, 'r') as f:
                classes = json.load(f)
        else:
            classes = list(model.config.id2label.values())

        return processor, model, classes
    except Exception as e:
        st.error(f"Failed to load Vision Transformer: {e}")
        return None, None, None

processor, model, class_names = load_vit_pipeline()

def format_label(raw_name: str) -> tuple:
    """Formats 'Tomato___Early_blight' into ('Tomato', 'Early Blight')."""
    if "___" in raw_name:
        plant, disease = raw_name.split("___", 1)
    else:
        plant, disease = "Plant", raw_name
    plant = plant.replace("_", " ").strip()
    disease = disease.replace("_", " ").strip()
    if disease.lower() == "healthy":
        disease = "Healthy (No Disease Detected)"
    return plant, disease

# Sidebar
st.sidebar.title("🌿 AI Vision Diagnostics")
st.sidebar.markdown(
    """
    **Architecture:** Vision Transformer (`google/vit-base-patch16-224`)  
    **Dataset:** PlantVillage + PlantDoc Field Injected  
    **Validation Accuracy:** **98.97%** (38 Disease Classes)  
    **Model Hub:** [RuougiShiki/crop-disease-vit](https://huggingface.co/RuougiShiki/crop-disease-vit)
    """
)

if class_names:
    with st.sidebar.expander("Supported Plants & Pathologies"):
        for name in class_names:
            p, d = format_label(name)
            st.write(f"- **{p}:** {d}")

# Main Layout
st.title("🌾 AI Crop Disease Detection")
st.markdown(
    "Upload a crop leaf photograph (in-field or lab shot) to diagnose diseases with high-confidence Vision Transformer predictions."
)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    uploaded_file = st.file_uploader(
        "Choose a crop leaf image...", 
        type=["jpg", "jpeg", "png", "webp"]
    )
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Leaf Image", use_container_width=True)

with col2:
    if uploaded_file is not None:
        if st.button("🔍 Analyze Leaf Condition", use_container_width=True, type="primary"):
            if model is None or processor is None:
                st.error("Model pipeline is unavailable.")
            else:
                with st.spinner("Analyzing leaf with Vision Transformer..."):
                    try:
                        inputs = processor(images=image, return_tensors="pt")
                        with torch.no_grad():
                            outputs = model(**inputs)
                            logits = outputs.logits
                            probabilities = torch.nn.functional.softmax(logits, dim=-1)[0]

                        # Top 3 predictions
                        top3_probs, top3_indices = torch.topk(probabilities, 3)
                        top_conf = top3_probs[0].item() * 100
                        top_raw_label = model.config.id2label[top3_indices[0].item()]
                        plant, disease = format_label(top_raw_label)

                        CONFIDENCE_THRESHOLD = 60.0

                        if top_conf < CONFIDENCE_THRESHOLD:
                            st.warning("⚠️ **Low Confidence / Unrecognized Sample**")
                            st.write(
                                f"Top prediction was **{plant} - {disease}** with only **{top_conf:.2f}%** confidence. "
                                "This image may not be a supported crop leaf or is obstructed."
                            )
                        else:
                            is_healthy = "healthy" in disease.lower()
                            if is_healthy:
                                st.success(f"### ✅ Result: {plant} is Healthy!")
                            else:
                                st.error(f"### 🚨 Disease Detected: {disease}")
                                st.markdown(f"**Crop Specie:** {plant}")

                            st.metric(label="Diagnostic Confidence", value=f"{top_conf:.2f}%")
                            st.progress(min(int(top_conf), 100))

                        # Detailed Probability Distribution
                        st.markdown("---")
                        st.subheader("Diagnostic Probability Distribution")
                        for prob, idx in zip(top3_probs, top3_indices):
                            p_crop, p_dis = format_label(model.config.id2label[idx.item()])
                            pct = prob.item() * 100
                            st.write(f"**{p_crop} - {p_dis}**: `{pct:.2f}%`")
                            st.progress(min(int(pct), 100))

                    except Exception as e:
                        st.error(f"Inference error: {e}")
    else:
        st.info("👈 Please upload an image on the left to start the analysis.")
