import os

from providers import ProviderFactory
from prompts.youtube_prompt import SYSTEM_PROMPT
from modules.project_manager import ProjectManager


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

        return self.provider.generate(
            SYSTEM_PROMPT,
            user_prompt
        )

    def save(
        self,
        project: dict,
        script: str
    ) -> str:

        filepath = os.path.join(
            project["root"],
            "script.txt"
        )

        with open(
            filepath,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(script)

        project["script"] = filepath

        return filepath

    def generate_project(
        self,
        topic: str
    ) -> dict:

        project = ProjectManager.create(topic)

        script = self.generate(topic)

        self.save(
            project,
            script
        )

        project["script_text"] = script

        return project