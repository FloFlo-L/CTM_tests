import pytest
from unittest.mock import patch

from Models.Player import Player
from Models.Tournament import Tournament
from Views.TournamentView import TournamentView
from Views.PlayerView import PlayerView

from Controllers.TournamentController import TournamentController


class TestTournamentController:
    @pytest.fixture
    def tournament_controller(self):
        return TournamentController()

    @patch.object(TournamentView, "get_tournament_info")
    def test_create_tournament(self, mock_get_tournament_info, tournament_controller):
        """
        Teste la méthode `create_tournament` de TournamentController.
        """
        # Configuration du mock
        mock_get_tournament_info.return_value = (
            "Test Tournament",
            "Paris",
            "01/01/2024",
            "15/01/2024",
            4,
            "Ceci est un tournoi de test",
        )

        # Appel de la méthode à tester
        tournament_controller.create_tournament()

        # Vérifications
        assert tournament_controller.tournament is not None
        assert isinstance(tournament_controller.tournament, Tournament)
        assert tournament_controller.tournament.name == "Test Tournament"
        assert tournament_controller.tournament.location == "Paris"
        assert tournament_controller.tournament.start_date == "01/01/2024"
        assert tournament_controller.tournament.end_date == "15/01/2024"
        assert tournament_controller.tournament.rounds == 4
        assert tournament_controller.tournament.description == "Ceci est un tournoi de test"

    @patch.object(Tournament, "get_tournaments")
    @patch.object(Player, "get_players")
    @patch.object(TournamentView, "select_tournament")
    @patch.object(PlayerView, "select_player")
    def test_add_player_to_tournament(
        self,
        mock_select_player,
        mock_select_tournament,
        mock_get_players,
        mock_get_tournaments,
        tournament_controller,
    ):
        """
        Teste la méthode `add_player_to_tournament` de TournamentController.
        """
        # Configuration des mocks
        mock_get_tournaments.return_value = [
            {
                "id": 1,
                "name": "Test Tournament",
                "location": "Paris",
                "start_date": "01/01/2024",
                "end_date": "15/01/2024",
                "rounds": 4,
                "player_list": [],
                "description": "Ceci est un tournoi de test",
            }
        ]
        mock_get_players.return_value = [
            {"id": 1, "first_name": "John", "last_name": "Doe", "birth_date": "01/01/1980", "national_chess_id": "AB12345"},
            {"id": 2, "first_name": "Jane", "last_name": "Doe", "birth_date": "01/01/1985", "national_chess_id": "AB12346"},
        ]
        mock_select_tournament.return_value = 1
        mock_select_player.return_value = 0

        # Appel de la méthode à tester
        tournament_controller.add_player_to_tournament()

        # Vérifications
        assert tournament_controller.tournament.player_list[0]["id"] == 1
