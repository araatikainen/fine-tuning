import json
import re
from pydantic import ValidationError
from models.sentiment import SentimentOutput

def reconstruct_json(json_data: str) -> SentimentOutput:
    """Reconstruct a JSON object from a string"""
    # Try find the sentiment and score fields from string
    try:
        # Use regex to extract JSON part (first occurrence of {...})
        json_match = re.search(r"\{.*?\}", json_data, re.DOTALL)
        if not json_match:
            raise ValueError("No valid JSON found in response.")

        json_str = json_match.group(0)  # Extract JSON string

        # Parse and validate JSON using Pydantic
        parsed_json = json.loads(json_str)
        return SentimentOutput(**parsed_json)  # Ensure it matches expected format

    except (json.JSONDecodeError, ValidationError) as e:
        raise ValueError(f"Error reconstructing JSON: {e}, Please try simplifying the request.")