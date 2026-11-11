"""
SpeakUP - AI Speech Analysis Microservice
Entrypoint and FastAPI application configuration.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.routers.speech_router import router as speech_router

app = FastAPI(
    title="SpeakUP - AI Speech Analysis",
    description="Microservice responsible for AI-based oral speech analysis.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Enable CORS for frontend and service integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include speech analysis router
app.include_router(speech_router)


@app.get("/", include_in_schema=False)
async def root_redirect():
    """Redirect root requests to interactive Swagger UI documentation."""
    return RedirectResponse(url="/docs")
