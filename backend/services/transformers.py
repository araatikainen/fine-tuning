from transformers import pipeline
from models.sentiment import SentimentOutput


def analyze_transformer(text: str) -> dict:
    """Analyze sentiment of text using a pre-trained model"""

    try:
        classifier = pipeline("sentiment-analysis", model="raati/distilbert_imdb_sentiment_analysis", tokenizer="raati/distilbert_imdb_sentiment_analysis_tokenizer")
        
        output = SentimentOutput(
            sentiment="positive" if classifier(text)[0]["label"] == "LABEL_1" else "negative", 
            score=classifier(text)[0]["score"]
            )
        
        return output
     
    except Exception as e:
        raise e