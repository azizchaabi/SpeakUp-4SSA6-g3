"""Pydantic schemas for AI Speech Analysis."""

from .speech_schema import (
    HelloResponse,
    LanguageEnum,
    LanguagesResponse,
    SpeechAnalyzeRequest,
    SpeechAnalyzeResponse,
    StatusResponse,
    SupportedLanguage,
)

__all__ = [
    "HelloResponse",
    "StatusResponse",
    "LanguageEnum",
    "SupportedLanguage",
    "LanguagesResponse",
    "SpeechAnalyzeRequest",
    "SpeechAnalyzeResponse",
]
