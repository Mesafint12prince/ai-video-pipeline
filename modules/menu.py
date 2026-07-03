from modules.script_generator import ScriptGenerator
from modules.voice_generator import VoiceGenerator
from modules.project_selector import ProjectSelector

def start_menu():

    while True:

        print("\n==============================")
        print("      AI VIDEO PIPELINE")
        print("==============================")

        print("1. Generate Script")
        print("2. Generate Voice")
        print("3. Full Pipeline")
        print("4. Settings")
        print("5. Exit")

        choice = input("\nSelect an option: ")

        # -----------------------------
        # Generate Script
        # -----------------------------
        if choice == "1":

            topic = input("\nEnter video topic:\n> ")

            print("\nGenerating script...\n")

            try:

                generator = ScriptGenerator()

                project = generator.generate_project(topic)

                print("=" * 60)
                print("GENERATED SCRIPT")
                print("=" * 60)

                print(project["script_text"])

                print("\n✅ Script generated successfully!")
                print(f"📄 Saved to:\n{project['script']}")

            except Exception as e:

                print(f"\n❌ Error:\n{e}")

            input("\nPress Enter to continue...")

        # -----------------------------
        # Generate Voice
        # -----------------------------
               # -----------------------------
        # Generate Voice
        # -----------------------------
        elif choice == "2":

            project = ProjectSelector.choose()

            if project is None:
                input("\nPress Enter to continue...")
                continue

            print("\nGenerating voice...\n")

            try:

                generator = VoiceGenerator()

                output = generator.generate(project)

                print("=" * 60)
                print("VOICE GENERATED")
                print("=" * 60)

                print(f"\n🎤 Saved to:\n{output}")

            except Exception as e:

                print(f"\n❌ Error:\n{e}")

            input("\nPress Enter to continue...")
        elif choice == "3":

            topic = input("\nEnter video topic:\n> ")

            print("\nRunning full pipeline...\n")

            try:

                script_generator = ScriptGenerator()
                voice_generator = VoiceGenerator()

                project = script_generator.generate_project(topic)

                voice_generator.generate(project)

                print("=" * 60)
                print("PIPELINE COMPLETED")
                print("=" * 60)

                print(f"\n📁 Project Folder:\n{project['root']}")
                print(f"\n📄 Script:\n{project['script']}")
                print(f"\n🎤 Voice:\n{project['voice']}")

            except Exception as e:

                print(f"\n❌ Error:\n{e}")

            input("\nPress Enter to continue...")

        # -----------------------------
        # Settings
        # -----------------------------
        elif choice == "4":

            print("\n⚙️ Settings module is coming soon.")

            input("\nPress Enter to continue...")

        # -----------------------------
        # Exit
        # -----------------------------
        elif choice == "5":

            print("\n👋 Goodbye!")

            break

        else:

            print("\n❌ Invalid choice.")