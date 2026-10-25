# 🌾 Vision Transformer (ViT) for Real-World Crop Disease Detection

[![Docker Image](https://img.shields.io/badge/Docker-ryougishikii%2Fcrop__disease__detection-blue?logo=docker)](https://hub.docker.com/repository/docker/ryougishikii/crop_disease_detection/general)
[![Model Architecture](https://img.shields.io/badge/Model-ViT--Base--Patch16--224-green)](https://huggingface.co/google/vit-base-patch16-224)
[![Validation Accuracy](https://img.shields.io/badge/Validation%20Accuracy-98.97%25-brightgreen)]()
[![Classes](https://img.shields.io/badge/Classes-38%20Pathologies-orange)]()

An end-to-end computer vision and agricultural pathology diagnostic application powered by a fine-tuned **Google Vision Transformer (`google/vit-base-patch16-224`)**.

Unlike standard models trained solely on clean laboratory backgrounds, this model was trained on a combined dataset of **PlantVillage** and in-field real-world leaf photos from **PlantDoc** (incorporating soil, hands, sunlight variations, and complex outdoor foliage).

---

## 🚀 Key Highlights

* **Model Architecture:** Vision Transformer (`ViT-Base-Patch16-224`, 12 Transformer layers, 12 attention heads, 768 hidden dimension).
* **Robust In-Field Generalization:** Augmented with heavy photometric and geometric variations (Albumentations color jitter, blur, and lighting distortions) to handle actual farm conditions.
* **Empirical Validation:** **98.97% Validation Accuracy** across **10,807 holdout images** with balanced Macro F1 (0.9897).
* **Multi-Class Pathology:** Covers **38 distinct classes** spanning Apples, Blueberries, Cherries, Corn, Grapes, Oranges, Peaches, Bell Peppers, Potatoes, Raspberries, Soybeans, Squash, Strawberries, and Tomatoes.
* **Lightweight & Fast:** Streamlit web application powered by CPU-optimized PyTorch inference. Containerized and ready to deploy anywhere via Docker.

---

## 📊 Performance & Validation Metrics

| Metric | Score |
| :--- | :--- |
| **Validation Accuracy** | **98.97%** |
| **Macro Average F1** | **0.9897** |
| **Weighted Average F1** | **0.9898** |
| **Validation Set Size** | 10,807 images |
| **Supported Classes** | 38 categories |

For detailed per-class precision, recall, and LaTeX tables for academic citations, see [`RESEARCH_PAPER_GUIDE.txt`](./RESEARCH_PAPER_GUIDE.txt).

---

## 🐳 Quickstart with Docker

Pull and run the pre-built container from Docker Hub:

```bash
docker run -d -p 7860:7860 ryougishikii/crop_disease_detection:latest
```

Open your browser and navigate to:
```
http://localhost:7860
```

---

## 💻 Local Installation & Development

### 1. Clone Repository
```bash
git clone https://github.com/ryougishikii/crop_disease_detection.git
cd crop_disease_detection
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install CPU PyTorch and requirements
pip install -r requirements.txt
```

### 3. Run Streamlit Application
```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```
CropDiseaseDetection/
├── app.py                         # Streamlit UI & ViT inference engine
├── best_vit_plant_model/          # Fine-tuned ViT weights, processor, and label map
│   ├── config.json
│   ├── model.safetensors
│   ├── preprocessor_config.json
│   └── classes.json
├── dockerfile                     # Multi-stage CPU-optimized Dockerfile
├── .dockerignore                  # Docker build exclusions
├── requirements.txt               # Production Python dependencies
├── RESEARCH_PAPER_GUIDE.txt       # Asset references & metrics for research publication
└── README.md                      # Documentation
```

---

## 📜 Supported Crop Diseases (38 Classes)

<details>
<summary>Click to view all 38 supported plant diseases</summary>

* **Apple:** Apple Scab, Black Rot, Cedar Apple Rust, Healthy
* **Blueberry:** Healthy
* **Cherry:** Powdery Mildew, Healthy
* **Corn (Maize):** Cercospora Leaf Spot (Gray Leaf Spot), Common Rust, Northern Leaf Blight, Healthy
* **Grape:** Black Rot, Esca (Black Measles), Leaf Blight (Isariopsis Leaf Spot), Healthy
* **Orange:** Huanglongbing (Citrus Greening)
* **Peach:** Bacterial Spot, Healthy
* **Pepper (Bell):** Bacterial Spot, Healthy
* **Potato:** Early Blight, Late Blight, Healthy
* **Raspberry:** Healthy
* **Soybean:** Healthy
* **Squash:** Powdery Mildew
* **Strawberry:** Leaf Scorch, Healthy
* **Tomato:** Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Two-Spotted Spider Mite, Target Spot, Tomato Yellow Leaf Curl Virus, Tomato Mosaic Virus, Healthy

</details>

---

## 📄 License
This project is open-source under the MIT License.
