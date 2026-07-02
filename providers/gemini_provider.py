import os

from dotenv import load_dotenv
from google import genai

from providers.base_provider import BaseProvider
from modules.settings_manager import load_settings

load_dotenv()


class GeminiProvider(BaseProvider):

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

    def generate(self, system_prompt: str, user_prompt: str) -> str:

        settings = load_settings()

        prompt = f"""
{system_prompt}

{user_prompt}
"""

        response = self.client.models.generate_content(
            model=settings["model"],
            contents=prompt
        )

        return response.text.strip()