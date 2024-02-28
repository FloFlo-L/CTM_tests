# Views/MatchView.py

class MatchView:
    def display_match_results(self, match, match_number, round_number):
        # Affiche les résultats possibles pour un match donné.

        # Args:
        #     match (obj): L'objet match contenant les détails du match.
        #     match_number (int): Le numéro du match.
        #     round_number (int): Le numéro du tour auquel appartient le match.

        # Returns:
        #     int: Le choix de l'utilisateur pour le résultat du match (1, 2 ou 3).
        print(f"Match {match_number} Round {round_number} - Résultats")
        print(f"1 - {match.player1['first_name']} {match.player1['last_name']}")
        print(f"2 - {match.player2['first_name']} {match.player2['last_name']}")
        print("3 - égalité")

        # Demander le choix de l'utilisateur
        user_choice = self.get_user_choice()
        return user_choice

    def get_user_choice(self):
        # Invite l'utilisateur à entrer son choix (1, 2 ou 3) et valide l'entrée.
        # Returns:
        #     int: Le choix de l'utilisateur validé.

        # Note:
        #     Cette méthode continue d'inviter l'utilisateur jusqu'à ce qu'un choix valide soit entré.
        while True:
            try:
                choice = int(input("Entrez votre choix (1, 2 ou 3): "))
                if choice not in [1, 2, 3]:
                    print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
                else:
                    return choice
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")
