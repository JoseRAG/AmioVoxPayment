# AmioVox Collections — Mock Payment Page

A simple Flask demo checkout page. **This is a mock / test page only — it accepts any card details and does not process, validate, or store real payments.**

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000

## Deploy to Railway

1. Push this repo to GitHub.
2. In Railway, create a new project → **Deploy from GitHub repo**.
3. Railway auto-detects Python, installs `requirements.txt`, and runs the `Procfile`.

No environment variables are required. Railway sets `$PORT` automatically.

## Files

- `app.py` — Flask app (checkout + success routes)
- `templates/index.html` — checkout form
- `templates/success.html` — confirmation page
- `requirements.txt` — dependencies
- `Procfile` — start command for Railway
