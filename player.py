import json

class Player:
    def __init__(self, chess_id, first_name, last_name, ranking):
        self.chess_id = chess_id
        self.first_name = first_name
        self.last_name = last_name
        self.ranking = ranking
        self.score = 0

    def add_score(self, points):
        self.score += points

    def to_json(self):
        return {
            "chess_id": self.chess_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "ranking": self.ranking,
            "score": self.score,
        }

    @classmethod
    def from_json(cls, data):
        p = cls(
            data["chess_id"],
            data["first_name"],
            data["last_name"],
            data["ranking"],
        )
        p.score = data.get("score", 0)
        return p
