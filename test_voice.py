from modules.script_generator import ScriptGenerator
from modules.voice_generator import VoiceGenerator


topic = "5 AI tools every programmer should know"

script_generator = ScriptGenerator()

project = script_generator.generate_project(topic)

voice_generator = VoiceGenerator()

voice_generator.generate(project)

print("\nPipeline completed successfully!\n")

print(project)