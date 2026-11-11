"""
Speech Service containing business logic for speech analysis endpoints.
Note: Machine Learning / AI models will be integrated in future milestones.
Current responses return simulated demonstrator data adhering to the defined schema.
"""

from app.schemas.speech_schema import (
    HelloResponse,
    LanguageEnum,
    LanguagesResponse,
    SpeechAnalyzeRequest,
    SpeechAnalyzeResponse,
    StatusResponse,
    SupportedLanguage,
)


class SpeechService:
    """Business service providing speech analysis and metadata."""

    @staticmethod
    def get_hello() -> HelloResponse:
        """Return a greeting message confirming microservice availability."""
        return HelloResponse(
            message="Hello! The SpeakUP AI Speech Analysis microservice is operational."
        )

    @staticmethod
    def get_status() -> StatusResponse:
        """Return the microservice operational health and version."""
        return StatusResponse(
            service="SpeakUP - AI Speech Analysis",
            status="UP",
            version="1.0.0"
        )

    @staticmethod
    def get_languages() -> LanguagesResponse:
        """Return supported languages for speech analysis."""
        return LanguagesResponse(
            languages=[
                SupportedLanguage(
                    code="fr",
                    name="French",
                    nativeName="Français"
                ),
                SupportedLanguage(
                    code="en",
                    name="English",
                    nativeName="English"
                ),
            ]
        )

    @staticmethod
    def analyze_speech(request: SpeechAnalyzeRequest) -> SpeechAnalyzeResponse:
        """
        Analyze speech input and calculate pronunciation, fluency, and intonation scores.

        Simulation Logic:
        - Computes dynamic realistic scores (0-100) based on input characteristics.
        - Produces personalized simulated pedagogical feedback depending on language.
        """
        clean_text = request.text.strip()
        word_count = len(clean_text.split())

        # Baseline simulated scores between 75 and 95 based on text length and variation
        base_factor = min(len(clean_text), 100) / 100.0
        pronunciation = round(80.0 + (base_factor * 12.0) % 15.0, 1)
        fluency = round(78.0 + (word_count * 3.5) % 18.0, 1)
        intonation = round(82.0 + (base_factor * 8.0) % 13.0, 1)

        # Weighted overall score
        overall = round(
            (pronunciation * 0.4) + (fluency * 0.35) + (intonation * 0.25),
            1
        )

        # Simulated contextual feedback by language
        if request.language == LanguageEnum.FR:
            if overall >= 85.0:
                feedback = (
                    "Très bonne prononciation et rythme fluide. "
                    "L'articulation des phonèmes est claire et l'intonation est naturelle."
                )
            else:
                feedback = (
                    "Bonne expression orale générale. "
                    "Pensez à soigner les liaisons et à moduler davantage votre intonation."
                )
        else:  # English
            if overall >= 85.0:
                feedback = (
                    "Great pronunciation and natural speech rhythm. "
                    "Vowel sounds are crisp and sentence stress is well modulated."
                )
            else:
                feedback = (
                    "Good overall oral performance. "
                    "Focus on word stress and smoothing transitions between connected words."
                )

        return SpeechAnalyzeResponse(
            transcription=clean_text,
            pronunciationScore=pronunciation,
            fluencyScore=fluency,
            intonationScore=intonation,
            overallScore=overall,
            feedback=feedback,
            isSimulated=True
        )
