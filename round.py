from datetime import datetime

class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start = datetime.now().isoformat()
        self.end = None

    def finish(self):
        self.end = datetime.now().isoformat()

    def to_json(self):
        return {
            "name": self.name,
            "matches": [m.to_json() for m in self.matches],
            "start": self.start,
            "end": self.end,
        }
