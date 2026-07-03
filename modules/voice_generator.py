import asyncio
import os

import edge_tts

from modules.voice_manager import VoiceManager


class VoiceGenerator:

    def __init__(self):

        self.manager = VoiceManager()

        self.voice = self.manager.get_voice()
        self.rate = self.manager.get_rate()

    def read_script(
        self,
        script_path: str
    ) -> str:

        with open(
            script_path,
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

    def generate_from_file(

        self,

        script_path: str

    ) -> str:

        if not os.path.exists(script_path):

            raise FileNotFoundError(
                f"Script not found:\n{script_path}"
            )

        text = self.read_script(script_path)

        output_path = script_path.replace(
            "_script.txt",
            "_voice.mp3"
        )

        asyncio.run(

            self._generate_voice(

                text,

                output_path

            )

        )

        return output_path