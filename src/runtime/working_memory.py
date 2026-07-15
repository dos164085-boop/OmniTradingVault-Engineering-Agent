class WorkingMemory:

    def __init__(self):

        self.clear()

    def set(self, key, value):

        self._memory[key] = value

    def get(self, key, default=None):

        return self._memory.get(key, default)

    def remove(self, key):

        self._memory.pop(key, None)

    def clear(self):

        self._memory = {}

    def update(self, values):

        self._memory.update(values)

    def snapshot(self):

        return dict(self._memory)

    def size(self):

        return len(self._memory)
    