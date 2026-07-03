from modules.settings_manager import (
    load_settings,
    save_settings
)


class VoiceManager:

    def __init__(self):
        self.settings = load_settings()

    def get_voice(self):

        return self.settings["voice"]["name"]

    def get_rate(self):

        return self.settings["voice"]["rate"]

    def set_voice(self, voice_name):

        self.settings["voice"]["name"] = voice_name

        save_settings(self.settings)

    def set_rate(self, rate):

        self.settings["voice"]["rate"] = rate

        save_settings(self.settings)