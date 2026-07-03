import os


class ProjectSelector:

    PROJECTS_FOLDER = "projects"

    @staticmethod
    def choose():

        if not os.path.exists(ProjectSelector.PROJECTS_FOLDER):
            print("\nNo projects found.")
            return None

        projects = []

        for folder in sorted(os.listdir(ProjectSelector.PROJECTS_FOLDER)):

            root = os.path.join(
                ProjectSelector.PROJECTS_FOLDER,
                folder
            )

            if not os.path.isdir(root):
                continue

            script_file = os.path.join(
                root,
                "script.txt"
            )

            if os.path.exists(script_file):
                projects.append(folder)

        if not projects:
            print("\nNo valid projects found.")
            return None

        print("\nAvailable Projects:\n")

        for index, project in enumerate(projects, start=1):
            print(f"{index}. {project}")

        while True:

            choice = input("\nSelect project: ")

            try:

                choice = int(choice)

                if 1 <= choice <= len(projects):
                    break

            except ValueError:
                pass

            print("Invalid selection.")

        root = os.path.join(
            ProjectSelector.PROJECTS_FOLDER,
            projects[choice - 1]
        )

        return {

            "root": root,

            "script": os.path.join(
                root,
                "script.txt"
            ),

            "voice": os.path.join(
                root,
                "voice.mp3"
            ),

            "images": os.path.join(
                root,
                "images"
            ),

            "assets": os.path.join(
                root,
                "assets"
            ),

            "subtitles": os.path.join(
                root,
                "subtitles"
            ),

            "final": os.path.join(
                root,
                "final"
            )

        }