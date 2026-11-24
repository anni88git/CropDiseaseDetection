# Ksetrin Backend

FastAPI backend for Ksetrin — deployed on **Render**.

## Setup on Render

1. Connect this `backend/` folder (or repo root set to `backend/`) to Render.
2. Set the following environment variables in Render dashboard:
   - `GROQ_API_KEY` — your Groq API key
   - `FRONTEND_URL` — your Vercel frontend URL (e.g. `https://ksetrin.vercel.app`)

## Local Development

```bash
pip install -r requirements.txt
uvicorn server:app --reload --port 8080
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/predict` | Upload leaf image file |
| POST | `/api/predict/json` | Base64 or sample name |
| GET | `/api/samples` | List sample images |
| GET | `/api/classes` | All 38 disease classes |
| POST | `/api/chat` | AI agronomist chat |
| GET | `/api/health` | Health check |
| GET | `/ping` | Keep-alive ping |
