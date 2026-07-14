import yaml

from .repository import Repository


class Incident:

    def __init__(self):
        self.repository = Repository()

    def incident_directory(self, incident_id):

        return (
            self.repository.agent_directory()
            / "knowledge"
            / "engineering"
            / "incidents"
            / incident_id
        )

    def _read_text(self, path):

        if not path.exists():
            return ""

        return path.read_text(encoding="utf-8").strip()

    def load(self, incident_id):

        directory = self.incident_directory(incident_id)

        if not directory.exists():
            raise FileNotFoundError(
                f"Incidente '{incident_id}' no encontrado."
            )

        with open(
            directory / "incident.yaml",
            "r",
            encoding="utf-8",
        ) as file:

            metadata = yaml.safe_load(file)

        return {
            "incident": metadata,
            "summary": self._read_text(directory / "summary.md"),
            "timeline": self._read_text(directory / "timeline.md"),
            "lessons": self._read_text(directory / "lessons-learned.md"),
        }