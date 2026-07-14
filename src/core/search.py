from pathlib import Path
import yaml

from src.core.repository import Repository


class SearchEngine:

    def __init__(self):

        self.repo = Repository()

        self.incidents_directory = (
            self.repo.agent_directory()
            / "knowledge"
            / "engineering"
            / "incidents"
        )

    def search(self, query):

        query = query.lower()

        results = []

        if not self.incidents_directory.exists():
            return results

        for incident_file in self.incidents_directory.glob("*/incident.yaml"):

            with open(incident_file, "r", encoding="utf-8") as f:

                incident = yaml.safe_load(f)

            if self._matches(incident, query):

                results.append(
                    {
                        "id": incident["id"],
                        "title": incident["title"],
                        "project": incident["project"],
                        "status": incident["status"],
                        "confidence": incident.get(
                            "confidence",
                            "Unknown"
                        ),
                        "patterns": incident.get(
                            "patterns",
                            []
                        ),
                    }
                )

        return results

    def _matches(self, incident, query):

        fields = [
            incident.get("id", ""),
            incident.get("title", ""),
            incident.get("project", ""),
            incident.get("category", ""),
            incident.get("status", ""),
            incident.get("summary", ""),
            incident.get("confidence", ""),
        ]

        for tag in incident.get("tags", []):

            fields.append(tag)

        for pattern in incident.get("patterns", []):

            fields.append(pattern)

        text = " ".join(fields).lower()

        return query in text