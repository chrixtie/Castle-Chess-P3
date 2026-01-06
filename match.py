class Match:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.result = None

    def record_result(self, score_p1, score_p2):
        self.result = (score_p1, score_p2)
        self.p1.add_score(score_p1)
        self.p2.add_score(score_p2)

    def to_json(self):
        return {
            "p1": self.p1.chess_id,
            "p2": self.p2.chess_id,
            "result": self.result,
        }
