from pydantic import BaseModel


class SentimentOutput(BaseModel):
    """Class for llm output validation"""
    sentiment: str
    score: float