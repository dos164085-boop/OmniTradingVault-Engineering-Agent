from pathlib import Path
import yaml


class Repository:

    def __init__(self):
        self.root = Path(__file__).resolve().parents[2]

    def agent_directory(self):
        return self.root / ".agent"

    def version_file(self):
        return self.agent_directory() / "version.yaml"

    def knowledge_directory(self):
        return self.agent_directory() / "knowledge"

    def projects_directory(self):
        return self.knowledge_directory() / "projects"

    def list_projects(self):

        projects = self.projects_directory()

        if not projects.exists():
            return []

        return sorted(
            [
                directory.name
                for directory in projects.iterdir()
                if directory.is_dir()
            ]
        )

    def load_version(self):

        version = self.version_file()

        if not version.exists():
            return {}

        with open(version, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
        