class Tournament:
    def __init__(self, name, location, players):
        self.name = name
        self.location = location
        self.players = players
        self.rounds = []

    def add_round(self, rnd):
        self.rounds.append(rnd)

    def generate_pairings(self):
        sorted_players = sorted(self.players, key=lambda x: x.ranking, reverse=True)
        matches = []

        for i in range(0, len(sorted_players), 2):
            match = Match(sorted_players[i], sorted_players[i + 1])
            matches.append(match)

        return matches

    def to_json(self):
        return {
            "name": self.name,
            "location": self.location,
            "players": [p.to_json() for p in self.players],
            "rounds": [r.to_json() for r in self.rounds],
        }
