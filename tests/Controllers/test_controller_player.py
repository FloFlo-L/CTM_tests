import pytest
from unittest.mock import patch
from Models.Player import Player
from Views.PlayerView import PlayerView
from Controllers.PlayerController import PlayerController


class TestPlayerController:
    @pytest.fixture
    def player_controller(self):
        return PlayerController()

    @patch.object(PlayerView, "get_player_info")
    def test_add_player(self, mock_get_player_info, player_controller):
        """
        Teste la méthode `add_player` de PlayerController.
        """
        # Configuration du mock
        mock_get_player_info.return_value = ("Firstname", "Lastname", "30/03/2001", "AB12345")

        # Appel de la méthode à tester
        player_controller.add_player()

        # Vérifications
        assert player_controller.player is not None
        assert isinstance(player_controller.player, Player)
        assert player_controller.player.first_name == "Firstname"
        assert player_controller.player.last_name == "Lastname"
        assert player_controller.player.birth_date == "30/03/2001"
        assert player_controller.player.national_chess_id == "AB12345"
