import os
from dotenv import load_dotenv

# load .env only for local development
load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Check .env or environment variables.")

CHROMA_PATH = os.getenv("CHROMA_PATH", "chroma")
DATA_PATH = os.getenv("DATA_PATH", "data")