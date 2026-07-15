from src.core.loader import KnowledgeLoader
from src.core.cache import KnowledgeCache
from src.core.search import SearchEngine
from src.core.learning import LearningEngine
from src.core.graph import KnowledgeGraph
from src.core.statistics import KnowledgeStatistics
from src.core.validator import KnowledgeValidator
from src.core.exporter import KnowledgeExporter


class KnowledgeRegistry:

    def __init__(self):

        self._services = {
            "loader": KnowledgeLoader(),
            "cache": KnowledgeCache(),
            "search": SearchEngine(),
            "learning": LearningEngine(),
            "graph": KnowledgeGraph(),
            "statistics": KnowledgeStatistics(),
            "validator": KnowledgeValidator(),
            "exporter": KnowledgeExporter(),
        }

    def get(self, name):

        return self._services[name]

    def services(self):

        return sorted(self._services.keys())

    def exists(self, name):

        return name in self._services
    