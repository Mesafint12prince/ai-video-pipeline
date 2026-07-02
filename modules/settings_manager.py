import json
import os


SETTINGS_FILE = os.path.join(
    "config",
    "settings.json"
)


def load_settings():

    with open(
        SETTINGS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_settings(settings):

    with open(
        SETTINGS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            settings,
            file,
            indent=4
        )