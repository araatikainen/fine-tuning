from pydantic import BaseModel
from typing import List, Dict, Optional


class RequestMessage(BaseModel):
    message: str


class ResponseMessage(BaseModel):
    status_code: int
    content: str


class AnalystRequest(BaseModel):
    text: str
    model: str


class AnalystResponse(BaseModel):
    sentiment: str
    score: float
