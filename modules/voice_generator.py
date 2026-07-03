import asyncio
import os

import edge_tts

from modules.voice_manager import VoiceManager


class VoiceGenerator:

    def __init__(self):

        manager = VoiceManager()

        self.voice = manager.get_voice()
        self.rate = manager.get_rate()

    def read_script(
        self,
        project: dict
    ) -> str:

        with open(
            project["script"],
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    async def _generate_voice(

        self,

        text: str,

        output_path: str

    ):

        communicate = edge_tts.Communicate(

            text=text,

            voice=self.voice,

            rate=self.rate

        )

        await communicate.save(output_path)

    def generate(
        self,
        project: dict
    ) -> str:

        text = self.read_script(project)

        output_path = os.path.join(
            project["root"],
            "voice.mp3"
        )

        asyncio.run(

            self._generate_voice(

                text,

                output_path

            )

        )

        project["voice"] = output_path

        return output_path