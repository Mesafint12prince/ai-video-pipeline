import os
import re
from datetime import datetime


class ProjectManager:

    PROJECTS_FOLDER = "projects"

    @staticmethod
    def slugify(text: str) -> str:

        text = text.lower()

        text = re.sub(r"[^a-z0-9]+", "_", text)

        return text.strip("_")

    @staticmethod
    def create(topic: str):

        slug = ProjectManager.slugify(topic)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        project_name = f"{timestamp}_{slug}"

        root = os.path.join(
            ProjectManager.PROJECTS_FOLDER,
            project_name
        )

        folders = {

            "root": root,

            "images": os.path.join(root, "images"),

            "assets": os.path.join(root, "assets"),

            "subtitles": os.path.join(root, "subtitles"),

            "final": os.path.join(root, "final")

        }

        for folder in folders.values():

            os.makedirs(
                folder,
                exist_ok=True
            )

        return folders