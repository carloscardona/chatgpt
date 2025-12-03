"""Pydantic schemas for the golf swing analysis API."""

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, HttpUrl, Field


class VideoInput(BaseModel):
    """Input payload describing the video to analyze."""

    video_url: HttpUrl = Field(..., description="Accessible URL for the swing video")
    perspective: Optional[str] = Field(
        None,
        description="Camera perspective such as 'down-the-line' or 'face-on'",
    )
    player_height_cm: Optional[float] = Field(
        None, description="Approximate player height to reduce scale ambiguity"
    )
    club_length_cm: Optional[float] = Field(
        None, description="Known club length used for metric scaling"
    )


class Segment(BaseModel):
    """Represents an annotated swing segment."""

    name: str
    start_time_s: float
    end_time_s: float
    notes: Optional[str] = None


class Metric(BaseModel):
    """Represents a computed swing metric."""

    name: str
    value: float
    unit: str
    interpretation: Optional[str] = None


class Comparison(BaseModel):
    """Comparison between the user swing and a professional reference."""

    pro_name: str
    summary: str
    strengths: List[str] = Field(default_factory=list)
    deltas: List[str] = Field(default_factory=list)
    reference_video: Optional[HttpUrl] = None


class AnalysisResponse(BaseModel):
    """Full response for an analysis request."""

    video_url: HttpUrl
    segments: List[Segment]
    key_metrics: List[Metric]
    coaching_cues: List[str]
    pro_comparisons: List[Comparison]
