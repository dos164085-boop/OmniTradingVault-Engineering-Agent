from datetime import date
from pathlib import Path

import yaml

from src.core.repository import Repository


class IncidentCreator:

    def __init__(self):

        self.repo = Repository()

        self.incidents_directory = (
            self.repo.agent_directory()
            / "knowledge"
            / "engineering"
            / "incidents"
        )

    def create(self, incident_id):

        incident_path = self.incidents_directory / incident_id

        if incident_path.exists():

            raise FileExistsError(
                f"El incidente '{incident_id}' ya existe."
            )

        self._create_directories(incident_path)

        self._create_incident_yaml(
            incident_path,
            incident_id
        )

        self._create_markdown_files(incident_path)

        return incident_path

    def _create_directories(self, incident_path):

        incident_path.mkdir(
            parents=True,
            exist_ok=False
        )

        for directory in (
            "decisions",
            "evidence",
            "hypotheses",
            "iterations",
        ):

            (incident_path / directory).mkdir()

    def _create_incident_yaml(
        self,
        incident_path,
        incident_id,
    ):

        incident = {
            "id": incident_id,
            "title": "",
            "project": "",
            "category": "",
            "status": "Draft",
            "severity": "",
            "priority": "",
            "opened": str(date.today()),
            "closed": "",
            "owner": "",
            "summary": "",
            "tags": [],
            "patterns": [],
            "confidence": "Low",
            "version": 1.0,
        }

        with open(
            incident_path / "incident.yaml",
            "w",
            encoding="utf-8",
        ) as file:

            yaml.safe_dump(
                incident,
                file,
                sort_keys=False,
                allow_unicode=True,
            )

    def _create_markdown_files(
        self,
        incident_path,
    ):

        files = {
            "summary.md":
                "# Summary\n\nPending...\n",

            "timeline.md":
                "# Timeline\n\nPending...\n",

            "lessons-learned.md":
                "# Lessons Learned\n\nPending...\n",
        }

        for filename, content in files.items():

            with open(
                incident_path / filename,
                "w",
                encoding="utf-8",
            ) as file:

                file.write(content)
                