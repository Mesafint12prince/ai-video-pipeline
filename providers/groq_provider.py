import os

from dotenv import load_dotenv
from groq import Groq

from providers.base_provider import BaseProvider

load_dotenv()


class GroqProvider(BaseProvider):

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)

    def generate(self, system_prompt: str, user_prompt: str) -> str:

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],

            temperature=0.8,
            max_tokens=600
        )

        return response.choices[0].message.content.strip()