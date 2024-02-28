from Views.TournamentView import TournamentView


class ReportView:
    def __init__(self):
        self.tournaments = TournamentView()

    def display_players_alphabetical(self, players):
        """
        Affiche la liste des joueurs par ordre alphabétique.

        Args:
            players (list): Liste des joueurs à afficher.
        """
        print("\nListe des joueurs par ordre alphabétique:")
        for player in players:
            print(f"{player['last_name']} {player['first_name']} (INE: {player['national_chess_id']})")

    def display_tournaments(self, tournaments):
        """
        Affiche la liste des tournois.

        Args:
            tournaments (list): Liste des tournois à afficher.
        """
        print("\nListe de tous les tournois :")
        for tournament in tournaments:
            print(tournament['name'])

    def display_tournament_infos(self, tournament):
        """
        Affiche les informations détaillées d'un tournoi.

        Args:
            tournament (dict): Dictionnaire contenant les informations du tournoi.
        """
        print("\nDétails du tournoi :")
        print(f"Nom: {tournament['name']}")
        print(f"Lieu: {tournament['location']}")
        print(f"Date de début: {tournament['start_date']}")
        print(f"Date de fin: {tournament['end_date']}")

    def display_tournament_players_alphabetical(self, players):
        """
        Affiche la liste des joueurs d'un tournoi par ordre alphabétique.

        Args:
            players (list): Liste des joueurs du tournoi à afficher.
        """
        print("\nListe des joueurs du tournoi par ordre alphabétique:")
        for player in players:
            print(f"{player['last_name']} {player['first_name']} (INE: {player['national_chess_id']})")

    def display_rounds_and_matches(self, tournament_name, rounds_list, players_sorted):
        """
        Affiche les rounds et les matches d'un tournoi spécifique.

        Args:
            tournament_name (str): Nom du tournoi.
            rounds_list (list): Liste des rounds et des matches du tournoi.
            players_sorted (list): Liste des joueurs triés.
        """
        print(f"\n{tournament_name}\n")
        for round_info in rounds_list:
            print(f"ROUND {round_info['Round']}\n")
            for idx, match in enumerate(round_info['matches']):
                player1, score1 = match[0]
                player2, score2 = match[1]
                print(f"MATCH {idx + 1}")
                print(f"{player1} vs {player2}")
                if score1 > score2:
                    print(f"Résultat: victoire {player1}\n")
                elif score2 > score1:
                    print(f"Résultat: victoire {player2}\n")
                else:
                    print("Résultat: égalité\n")

        self.display_tournament_player_ranking(players_sorted)

    def display_tournament_player_ranking(self, players):
        """
        Affiche le classement des joueurs dans le tournoi.

        Args:
            players (list): Liste des joueurs du tournoi avec leur score.
        """
        print("\nClassement des joueurs dans le tournoi :\n")
        for index, player in enumerate(players, start=1):
            print(f"{index}. {player['first_name']} {player['last_name']} - Score: {player['score']}")
