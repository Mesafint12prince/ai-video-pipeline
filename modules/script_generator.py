import os

from providers import ProviderFactory

from prompts.youtube_prompt import SYSTEM_PROMPT


class ScriptGenerator:

    def __init__(self):

        self.provider = ProviderFactory.create()

    def generate(
        self,
        topic: str
    ) -> str:

        user_prompt = f"""
Topic:
{topic}
"""

        script = self.provider.generate(
            SYSTEM_PROMPT,
            user_prompt
        )

        return script

    def save(
        self,
        topic: str,
        script: str
    ) -> str:

        os.makedirs(
            "output",
            exist_ok=True
        )

        filename = (
            topic.lower()
            .replace(" ", "_")
            + "_script.txt"
        )

        filepath = os.path.join(
            "output",
            filename
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(script)

        return filepath

    def generate_and_save(
        self,
        topic: str
    ):

        script = self.generate(topic)
        
        filepath = self.save(
            topic,
            script
        )

        return script, filepath
    