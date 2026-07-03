from modules.file_selector import FileSelector
from modules.voice_generator import VoiceGenerator

path = FileSelector.choose_script()

if path:

    generator = VoiceGenerator()

    mp3 = generator.generate_from_file(path)

    print("\nVoice created successfully!")
    print(mp3)