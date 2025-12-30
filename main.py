from models.player import Player
from models.tournament import Tournament
from controllers.tournament_controller import TournamentController
from views.console_view import show_players, show_tournament_info

p1 = Player("C001", "Alice", "Smith")
p2 = Player("C002", "Bob", "Jones")

tournament = Tournament("Castle Open", "Community Hall")
tournament.add_player(p1)
tournament.add_player(p2)

controller = TournamentController()
matches = controller.create_matches(tournament.players)

matches[0].set_result("1-0")

show_tournament_info(tournament)
show_players(tournament.players)

tournament.save_to_file("data/tournaments.json")