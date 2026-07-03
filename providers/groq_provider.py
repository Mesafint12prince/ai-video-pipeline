import os

from dotenv import load_dotenv
from groq import Groq

from providers.base_provider import BaseProvider
from modules.settings_manager import load_settings

load_dotenv()


class GroqProvider(BaseProvider):

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=api_key)

    def generate(self, system_prompt: str, user_prompt: str) -> str:

        settings = load_settings()

        response = self.client.chat.completions.create(

            model=settings["model"],

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

            temperature=settings["temperature"],
            max_tokens=settings["max_tokens"]
        )

        return response.choices[0].message.content.strip()