from src.core.indexer import KnowledgeIndexer


class KnowledgeGraph:

    def __init__(self):

        self.indexer = KnowledgeIndexer()

    def projects(self):

        graph = {}

        for incident in self.indexer.incidents():

            project = incident["incident"].get("project")

            if not project:
                continue

            graph.setdefault(project, [])

            graph[project].append(
                incident["incident"]["id"]
            )

        return graph

    def patterns(self):

        graph = {}

        for incident in self.indexer.incidents():

            incident_id = incident["incident"]["id"]

            for pattern in incident["incident"].get(
                "patterns",
                [],
            ):

                graph.setdefault(pattern, [])

                graph[pattern].append(incident_id)

        return graph

    def summary(self):

        return {
            "projects": self.projects(),
            "patterns": self.patterns(),
        }
    