from enum import Enum
from typing import List
from pydantic import BaseModel, ConfigDict, Field


class LanguageEnum(str, Enum):
    """Supported spoken languages."""
    FR = "fr"
    EN = "en"


class HelloResponse(BaseModel):
    """Response schema for service greeting endpoint."""
    message: str = Field(
        ...,
        description="Greeting and operational confirmation message.",
        examples=["Hello! The AI Speech Analysis microservice is up and running successfully."]
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "message": "Hello! The AI Speech Analysis microservice is up and running successfully."
            }
        }
    )


class StatusResponse(BaseModel):
    """Response schema for service status endpoint."""
    service: str = Field(
        ...,
        description="Name of the microservice.",
        examples=["SpeakUP - AI Speech Analysis"]
    )
    status: str = Field(
        ...,
        description="Current operational status of the service.",
        examples=["UP"]
    )
    version: str = Field(
        ...,
        description="Version of the microservice.",
        examples=["1.0.0"]
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "SpeakUP - AI Speech Analysis",
                "status": "UP",
                "version": "1.0.0"
            }
        }
    )


class SupportedLanguage(BaseModel):
    """Details about a supported language."""
    code: str = Field(
        ...,
        description="ISO 639-1 two-letter language code.",
        examples=["fr"]
    )
    name: str = Field(
        ...,
        description="Language name in English.",
        examples=["French"]
    )
    nativeName: str = Field(
        ...,
        description="Language name in its native script.",
        examples=["Français"]
    )


class LanguagesResponse(BaseModel):
    """Response schema listing supported languages."""
    languages: List[SupportedLanguage] = Field(
        ...,
        description="List of supported languages for speech analysis."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "languages": [
                    {"code": "fr", "name": "French", "nativeName": "Français"},
                    {"code": "en", "name": "English", "nativeName": "English"}
                ]
            }
        }
    )


class SpeechAnalyzeRequest(BaseModel):
    """Request schema for speech analysis submission."""
    language: LanguageEnum = Field(
        ...,
        description="Language of the spoken input ('fr' for French, 'en' for English).",
        examples=["fr"]
    )
    text: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Spoken text uttered by the learner to analyze.",
        examples=["Bonjour, je suis ravi de participer à cette séance d'entraînement oral."]
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "language": "fr",
                "text": "Bonjour, je suis ravi de participer à cette séance d'entraînement oral."
            }
        }
    )


class SpeechAnalyzeResponse(BaseModel):
    """
    Response schema returning speech analysis metrics.
    Note: In this version, all returned scores and metrics are simulated mock data
    for demonstration and contract verification purposes.
    """
    transcription: str = Field(
        ...,
        description="Transcribed text from the audio (simulated from input for this version).",
        examples=["Bonjour, je suis ravi de participer à cette séance d'entraînement oral."]
    )
    pronunciationScore: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Simulated pronunciation accuracy score (0 - 100).",
        examples=[88.5]
    )
    fluencyScore: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Simulated fluency score evaluating pauses, rhythm, and speed (0 - 100).",
        examples=[91.0]
    )
    intonationScore: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Simulated intonation and pitch modulation score (0 - 100).",
        examples=[84.0]
    )
    overallScore: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Simulated overall combined score (0 - 100).",
        examples=[87.8]
    )
    feedback: str = Field(
        ...,
        description="Simulated pedagogical feedback and guidance for the learner.",
        examples=["Bonne élocution et intonation naturelle. Travaillez les liaisons sur les consonnes finales."]
    )
    isSimulated: bool = Field(
        default=True,
        description="Indicator showing that metrics are simulated demonstration values."
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "transcription": "Bonjour, je suis ravi de participer à cette séance d'entraînement oral.",
                "pronunciationScore": 88.5,
                "fluencyScore": 91.0,
                "intonationScore": 84.0,
                "overallScore": 87.8,
                "feedback": "Bonne élocution et intonation naturelle. Travaillez les liaisons sur les consonnes finales.",
                "isSimulated": True
            }
        }
    )
