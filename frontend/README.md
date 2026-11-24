# Ksetrin Frontend

This is the static frontend for Ksetrin — deployed on **Vercel**.

## Setup

1. Set the backend URL in both `index.html` and `login.html`:
   - Find `const BACKEND_URL = 'https://YOUR-RENDER-BACKEND.onrender.com';`
   - Replace with your actual Render backend URL.

2. Deploy this `frontend/` folder to Vercel:
   ```bash
   vercel --cwd frontend/
   ```
   Or connect your GitHub repo to Vercel and set the **Root Directory** to `frontend`.

## Environment

No build step needed — pure static HTML/CSS/JS.
