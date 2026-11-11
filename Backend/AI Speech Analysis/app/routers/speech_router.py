"""API routes for speech analysis and service health endpoints."""

from fastapi import APIRouter, HTTPException, status

from app.schemas.speech_schema import (
    HelloResponse,
    LanguagesResponse,
    SpeechAnalyzeRequest,
    SpeechAnalyzeResponse,
    StatusResponse,
)
from app.services.speech_service import SpeechService

router = APIRouter(
    prefix="/api/speech",
    tags=["Speech Analysis"]
)


@router.get(
    "/hello",
    response_model=HelloResponse,
    status_code=status.HTTP_200_OK,
    summary="Microservice Greeting",
    description="Confirms that the AI Speech Analysis microservice is reachable and operational."
)
async def get_hello() -> HelloResponse:
    """Return greeting confirmation message."""
    return SpeechService.get_hello()


@router.get(
    "/status",
    response_model=StatusResponse,
    status_code=status.HTTP_200_OK,
    summary="Microservice Health Status",
    description="Returns the microservice identification, current health state, and version."
)
async def get_status() -> StatusResponse:
    """Return service status and version."""
    return SpeechService.get_status()


@router.get(
    "/languages",
    response_model=LanguagesResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Supported Languages",
    description="Returns the list of spoken languages supported by the speech analysis engine (French and English)."
)
async def get_languages() -> LanguagesResponse:
    """Return supported languages."""
    return SpeechService.get_languages()


@router.post(
    "/analyze",
    response_model=SpeechAnalyzeResponse,
    status_code=status.HTTP_200_OK,
    summary="Analyze Spoken Speech",
    description=(
        "Analyzes learner spoken input in the specified language (French 'fr' or English 'en') "
        "and returns simulated pronunciation, fluency, intonation, overall scores, and pedagogical feedback. "
        "**Note:** In this demonstration phase, metrics are simulated and do not require heavy ML models."
    ),
    responses={
        400: {
            "description": "Bad Request - Text is empty or contains only whitespace.",
            "content": {
                "application/json": {
                    "example": {"detail": "Text cannot be empty or blank."}
                }
            }
        },
        422: {
            "description": "Validation Error - Invalid language code or malformed body."
        }
    }
)
async def analyze_speech(payload: SpeechAnalyzeRequest) -> SpeechAnalyzeResponse:
    """Process speech input and return pronunciation, fluency, intonation, and feedback."""
    if not payload.text or not payload.text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text cannot be empty or contain only blank spaces."
        )

    return SpeechService.analyze_speech(payload)
