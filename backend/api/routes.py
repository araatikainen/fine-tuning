import os
import requests
from fastapi import APIRouter, HTTPException
from models.requests import RequestMessage, ResponseMessage, AnalystRequest, AnalystResponse
from services.groq import translate_text, analyze_llama
from services.transformers import analyze_transformer

router = APIRouter()

@router.post("/test")
def generate():
    """Endpoint to test the model"""

    return {"message": "Hello from API"}
        

# week 2 task
@router.post("/generate")
def generate_message(request: RequestMessage):
    """Endpoint to generate a message"""
    try:
        print(request.message)
        result = translate_text(request.message)
        print(result)
        return ResponseMessage(status_code=200, content=result)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/analyze")
def analyze_sentiment(request: AnalystRequest):
    """Endpoint to analyze text"""
    try:

        if request.model == "custom":
            result = analyze_transformer(request.text)

        elif request.model == "llama":
            result = analyze_llama(request.text)
        else:
            raise HTTPException(status_code=400, detail="Invalid model, provide 'custom' or 'llama'")
        return AnalystResponse(sentiment=result.sentiment, score=result.score)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
