import yaml

from .repository import Repository


class IncidentRepository:

    def __init__(self):
        self.repository = Repository()

    def incidents_directory(self):
        return (
            self.repository.agent_directory()
            / "knowledge"
            / "engineering"
            / "incidents"
        )

    def list(self):

        root = self.incidents_directory()

        if not root.exists():
            return []

        incidents = []

        for directory in sorted(root.iterdir()):

            if not directory.is_dir():
                continue

            metadata = directory / "incident.yaml"

            if not metadata.exists():
                continue

            with open(metadata, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            incidents.append(
                {
                    "id": data["id"],
                    "status": data["status"],
                    "title": data["title"],
                    "project": data["project"],
                }
            )

        return incidents
    