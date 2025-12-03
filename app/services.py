"""Service layer with placeholder swing analysis logic."""

from __future__ import annotations

from typing import List

from .schemas import AnalysisResponse, Comparison, Metric, Segment, VideoInput


class SwingAnalysisService:
    """Stubbed service to orchestrate swing analysis tasks."""

    @staticmethod
    def analyze(video: VideoInput) -> AnalysisResponse:
        """Run the analysis pipeline.

        This function currently returns deterministic sample data while the
        actual computer vision and physics modeling pipelines are under
        development.
        """

        segments = SwingAnalysisService._build_segments()
        metrics = SwingAnalysisService._build_metrics()
        comparisons = SwingAnalysisService._build_comparisons()
        cues = SwingAnalysisService._build_cues()

        return AnalysisResponse(
            video_url=video.video_url,
            segments=segments,
            key_metrics=metrics,
            coaching_cues=cues,
            pro_comparisons=comparisons,
        )

    @staticmethod
    def _build_segments() -> List[Segment]:
        return [
            Segment(name="Address", start_time_s=0.0, end_time_s=0.7, notes="Stable base"),
            Segment(
                name="Top",
                start_time_s=0.7,
                end_time_s=1.4,
                notes="Full shoulder turn with controlled tempo",
            ),
            Segment(
                name="Impact",
                start_time_s=1.5,
                end_time_s=1.6,
                notes="Hands ahead of clubhead with forward shaft lean",
            ),
            Segment(
                name="Finish",
                start_time_s=1.6,
                end_time_s=2.2,
                notes="Balanced hold with belt buckle facing target",
            ),
        ]

    @staticmethod
    def _build_metrics() -> List[Metric]:
        return [
            Metric(
                name="Clubhead speed",
                value=98.4,
                unit="mph",
                interpretation="On track for a mid-handicap driver swing; potential +4–6 mph with better ground use",
            ),
            Metric(
                name="X-factor stretch",
                value=18.2,
                unit="deg",
                interpretation="Separation between pelvis and thorax during transition is modest; room to increase for speed",
            ),
            Metric(
                name="Attack angle",
                value=+2.4,
                unit="deg",
                interpretation="Slightly upward, good for maximizing carry with driver",
            ),
            Metric(
                name="Low-point control",
                value=2.1,
                unit="in fwd",
                interpretation="Consistent forward low point; improves contact with irons",
            ),
        ]

    @staticmethod
    def _build_comparisons() -> List[Comparison]:
        return [
            Comparison(
                pro_name="Rory McIlroy",
                summary=(
                    "Similar tempo; Rory opens pelvis sooner in transition which shallows the club and frees rotation."
                ),
                strengths=["Balanced finish", "Neutral club path"],
                deltas=["Later trail elbow adduction", "Less early wrist flexion"],
                reference_video="https://example.com/rory-down-the-line.mp4",
            ),
            Comparison(
                pro_name="Nelly Korda",
                summary=(
                    "Nelly maintains more spine inclination through impact, limiting early extension and stabilizing face control."
                ),
                strengths=["Great rhythm", "Centered pressure shift"],
                deltas=["More stable head during downswing"],
                reference_video="https://example.com/nelly-face-on.mp4",
            ),
        ]

    @staticmethod
    def _build_cues() -> List[str]:
        return [
            "Feel the lead hip clear earlier to open space for the trail arm",
            "Keep trail wrist hinged longer to shallow the club in transition",
            "Stay in posture through impact—imagine your belt buckle stays back until after strike",
        ]
