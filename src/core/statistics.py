from collections import Counter

from src.core.indexer import KnowledgeIndexer


class KnowledgeStatistics:

    def __init__(self):

        self.indexer = KnowledgeIndexer()

    def summary(self):

        incidents = self.indexer.incidents()

        projects = Counter()
        status = Counter()
        patterns = Counter()

        for incident in incidents:

            metadata = incident["incident"]

            project = metadata.get("project")

            if project:
                projects[project] += 1

            incident_status = metadata.get("status")

            if incident_status:
                status[incident_status] += 1

            for pattern in metadata.get("patterns", []):

                patterns[pattern] += 1

        return {
            "total_incidents": len(incidents),
            "projects": dict(projects),
            "status": dict(status),
            "patterns": dict(patterns),
            "total_projects": len(projects),
            "total_patterns": len(patterns),
        }