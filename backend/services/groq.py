import json
import os
from pydantic import ValidationError
from groq import Groq
from models.sentiment import SentimentOutput
from services.validate_json import reconstruct_json

def analyze_llama(text: str):
    """Analyze text using a groq api"""
    try:
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

        system_message = """
        You are a sentiment analysis assistant. Analyze the given text and return a JSON object with two fields:
        - "sentiment": Either "positive" or "negative".
        - "score": A float between 0 and 1 representing confidence in classification.
        
        Example output:
        {"sentiment": "positive", "score": 0.87}
        """

        sentiment_analysis = client.chat.completions.create(
            messages=[{
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": text
                }
            ],

            model="llama-3.3-70b-versatile",
            temperature=0.5,
            stream=False,
        )
        print(sentiment_analysis.choices[0])
        response = sentiment_analysis.choices[0].message.content

        # Try parsing JSON response
        try:
            sentiment_data = json.loads(response)
            return SentimentOutput(**sentiment_data)  # Validate with Pydantic
        except (json.JSONDecodeError, ValidationError):
            return reconstruct_json(response)

    except Exception as e:
        raise e

def translate_text(text: str):

    try:
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            #
            # Required parameters
            #
            messages=[{
                    "role": "system",
                    "content": "you are a helpful translator assistant. Your task is to translate the text from English to Finnish."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            stream=False,
        )

        print(chat_completion.choices[0])
        return chat_completion.choices[0].message.content

    except Exception as e:
        raise e
    