from providers.gemini_provider import generate

from prompts.youtube_prompt import SYSTEM_PROMPT

import os


def create_script(topic):

    script = generate(
        SYSTEM_PROMPT,
        f"Topic:\n{topic}"
    )

    os.makedirs("output", exist_ok=True)

    filename = topic.lower().replace(" ", "_")

    filepath = f"output/{filename}_script.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(script)

    return filepath