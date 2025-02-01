import os
from groq import Groq


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
    