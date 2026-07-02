from providers.gemini_provider import GeminiProvider
from providers.groq_provider import GroqProvider

from modules.settings_manager import load_settings


class ProviderFactory:

    @staticmethod
    def create():

        settings = load_settings()

        provider = settings["provider"].lower()

        if provider == "gemini":
            return GeminiProvider()

        elif provider == "groq":
            return GroqProvider()

        raise ValueError(
            f"Unknown provider: {provider}"
        )