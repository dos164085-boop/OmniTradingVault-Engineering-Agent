from src.core.incident import Incident
from src.core.incidents import IncidentRepository


class KnowledgeIndexer:

    def __init__(self):

        self.repository = IncidentRepository()
        self.incident = Incident()

    def incidents(self):

        incidents = []

        for item in self.repository.list():

            incidents.append(
                self.incident.load(item["id"])
            )

        return incidents

    def projects(self):

        projects = set()

        for incident in self.incidents():

            project = incident["incident"].get("project")

            if project:
                projects.add(project)

        return sorted(projects)

    def patterns(self):

        patterns = set()

        for incident in self.incidents():

            for pattern in incident["incident"].get(
                "patterns",
                [],
            ):

                patterns.add(pattern)

        return sorted(patterns)

    def statistics(self):

        incidents = self.incidents()

        return {
            "incidents": len(incidents),
            "projects": len(self.projects()),
            "patterns": len(self.patterns()),
        }