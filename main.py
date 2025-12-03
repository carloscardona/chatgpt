"""FastAPI application exposing golf swing analysis endpoints."""

from __future__ import annotations

import uvicorn
from fastapi import FastAPI

from app.schemas import AnalysisResponse, VideoInput
from app.services import SwingAnalysisService

app = FastAPI(
    title="Golf Swing Analysis API",
    description=(
        "Upload swing footage, receive segmentation-aware analytics, physics-informed "
        "metrics, and comparisons to professional golfers."
    ),
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Health probe endpoint."""

    return {"status": "ok"}


@app.post("/analyze", response_model=AnalysisResponse, tags=["analysis"])
def analyze(video: VideoInput) -> AnalysisResponse:
    """Trigger a swing analysis job.

    The current implementation returns curated sample data while a full
    computer-vision pipeline (segmentation, 3D pose, physics modeling)
    is under construction.
    """

    return SwingAnalysisService.analyze(video)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
