from src.core.loader import KnowledgeLoader


class KnowledgeCache:

    def __init__(self):

        self.loader = KnowledgeLoader()
        self._incidents = None

    def incidents(self):

        if self._incidents is None:
            self.refresh()

        return self._incidents

    def refresh(self):

        self._incidents = self.loader.load()

        return self._incidents

    def clear(self):

        self._incidents = None

    def size(self):

        return len(self.incidents())
    