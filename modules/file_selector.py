import os


class FileSelector:

    OUTPUT_FOLDER = "output"

    @staticmethod
    def get_script_files():

        if not os.path.exists(FileSelector.OUTPUT_FOLDER):
            return []

        return sorted([
            file
            for file in os.listdir(FileSelector.OUTPUT_FOLDER)
            if file.endswith("_script.txt")
        ])

    @staticmethod
    def choose_script():

        files = FileSelector.get_script_files()

        if not files:
            print("\nNo script files found.")
            return None

        print("\nAvailable Scripts\n")

        for index, file in enumerate(files, start=1):
            print(f"{index}. {file}")

        while True:

            choice = input("\nSelect a script: ")

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(files):

                return os.path.join(
                    FileSelector.OUTPUT_FOLDER,
                    files[choice - 1]
                )

            print("Invalid selection.")