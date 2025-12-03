# Golf Swing Analysis Web App

A FastAPI-based web experience that accepts a swing video URL and returns segmentation-aware, physics-inspired analysis with suggested coaching cues and comparisons to professional golfers. The current implementation serves curated sample data while a full computer vision pipeline is being built.

## Quickstart

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Open the web UI**
   - Navigate to [http://localhost:8000/](http://localhost:8000/) and submit a swing video URL. The page uses the same API that powers the backend.

4. **Check health via API**
   ```bash
   curl http://localhost:8000/health
   ```

5. **Request an analysis via API**
   ```bash
   curl -X POST http://localhost:8000/analyze \
     -H "Content-Type: application/json" \
     -d '{"video_url": "https://example.com/swing.mp4", "perspective": "down-the-line"}'
   ```

## Response shape

- `segments`: key swing phases with timing and notes
- `key_metrics`: physics-inspired metrics like clubhead speed, X-factor stretch, attack angle
- `coaching_cues`: actionable drills or focus points
- `pro_comparisons`: summaries against curated professional reference swings

The payloads are defined in `app/schemas.py`, and the sample response is assembled in `app/services.py`.
