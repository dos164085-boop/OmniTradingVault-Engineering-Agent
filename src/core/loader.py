from src.core.indexer import KnowledgeIndexer


class KnowledgeLoader:

    def __init__(self):

        self.indexer = KnowledgeIndexer()

    def load(self):

        return self.indexer.incidents()

    def projects(self):

        projects = {}

        for incident in self.load():

            project = incident["incident"].get("project")

            if not project:
                continue

            projects.setdefault(project, [])

            projects[project].append(incident)

        return projects

    def incident(self, incident_id):

        for incident in self.load():

            if incident["incident"]["id"] == incident_id:
                return incident

        return None