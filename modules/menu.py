from modules.script_generator import ScriptGenerator
from modules.voice_generator import VoiceGenerator
from modules.file_selector import FileSelector


def start_menu():

    while True:

        print("\n==============================")
        print(" AI VIDEO PIPELINE")
        print("==============================")

        print("1. Generate Script")
        print("2. Generate Voice")
        print("3. Full Pipeline")
        print("4. Settings")
        print("5. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":

            topic = input("\nEnter video topic:\n> ")

            print("\nGenerating script...\n")

            try:

                generator = ScriptGenerator()

                script, filepath = generator.generate_and_save(topic)

                print("=" * 50)
                print("GENERATED SCRIPT")
                print("=" * 50)
                print(script)

                print("\n✅ Script generated successfully!")
                print(f"📄 Saved to: {filepath}")

            except Exception as e:

                print(f"\n❌ Error: {e}")

            input("\nPress Enter to continue...")

        elif choice == "2":

            script_path = FileSelector.choose_script()

            if script_path:

                print("\nGenerating voice...\n")

                try:

                    generator = VoiceGenerator()

                    output = generator.generate_from_file(
                        script_path
                    )

                    print("=" * 50)
                    print("VOICE GENERATED")
                    print("=" * 50)

                    print(f"\n✅ Saved to:\n{output}")

                except Exception as e:

                    print(f"\n❌ Error:\n{e}")

            input("\nPress Enter to continue...")

        elif choice == "3":

            print("\nFull Pipeline is not implemented yet.")

            input("\nPress Enter to continue...")

        elif choice == "4":

            print("\nSettings is not implemented yet.")

            input("\nPress Enter to continue...")

        elif choice == "5":

            print("\nGoodbye!")

            break

        else:

            print("\n❌ Invalid choice.")