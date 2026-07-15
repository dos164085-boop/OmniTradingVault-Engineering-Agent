from src.core.loader import KnowledgeLoader
from src.core.search import SearchEngine
from src.core.learning import LearningEngine
from src.core.statistics import KnowledgeStatistics
from src.core.graph import KnowledgeGraph
from src.core.validator import KnowledgeValidator


class KnowledgeService:

    def __init__(self):

        self.loader = KnowledgeLoader()
        self.search_engine = SearchEngine()
        self.learning_engine = LearningEngine()
        self.statistics_engine = KnowledgeStatistics()
        self.graph_engine = KnowledgeGraph()
        self.validator = KnowledgeValidator()

    def incidents(self):

        return self.loader.load()

    def incident(self, incident_id):

        return self.loader.incident(incident_id)

    def search(self, query):

        return self.search_engine.search(query)

    def learn(self, incident_id):

        return self.learning_engine.learn(incident_id)

    def statistics(self):

        return self.statistics_engine.summary()

    def graph(self):

        return self.graph_engine.summary()

    def validate(self):

        return self.validator.summary()
    