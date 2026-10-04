import os

from dotenv import load_dotenv
from agno.models.google import Gemini

load_dotenv()

DEFAULT_MODEL_ID = "gemini-3.5-flash-lite"
FALLBACK_MODEL_ID = "gemini-2.5-flash"


def get_model():
    return Gemini(
        id=os.getenv("MODEL_NAME", DEFAULT_MODEL_ID),
        api_key=os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"),
        temperature=0,
        retries=2,
        delay_between_retries=2,
        exponential_backoff=True,
    )


def get_fallback_models() -> list[Gemini]:
    return [
        Gemini(
            id=os.getenv("FALLBACK_MODEL_NAME", FALLBACK_MODEL_ID),
            api_key=os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY"),
            temperature=0,
        )
    ]
