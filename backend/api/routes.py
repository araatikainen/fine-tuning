import os
import requests
from fastapi import APIRouter, HTTPException
from models.requests import RequestMessage, ResponseMessage
from services.groq import translate_text

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
        result = translate_text(request.message)
        print(result)
        return ResponseMessage(status_code=200, content=result)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
