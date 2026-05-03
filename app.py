from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from query_rag import query_rag  
from create_and_populate_db import create_and_populate_db # your existing function
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
# Initialize FastAPI app
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


app = FastAPI(
    title="RAG API",
    description="API for querying documents using a RAG pipeline",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)






# 🔥 Run ingestion at startup (correct way)
@app.on_event("startup")
def startup_event():
    print("Running ingestion...")
    create_and_populate_db()


# Request schema
class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"status": "RAG API is running"}




@app.post("/query")
def ask_question(request: QueryRequest):
    try:
        if not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")

        answer = query_rag(request.query)

        return {
            "query": request.query,
            "answer": answer
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))