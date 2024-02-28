class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.winner = None

    def serialize(self):
        """
        Convertit l'objet Match en un dictionnaire pour faciliter la sauvegarde ou l'exportation.

        Returns:
            dict: Un dictionnaire représentant le match.
        """
        return {
            'player1': self.player1,
            'player2': self.player2,
            'winner': self.winner
        }

    def __str__(self):
        """
        Fournit une chaîne de caractères de l'objet Match, montrant les deux joueurs en compétition.

        Returns:
            str: Chaîne représentant le match.
        """
        return (f"{self.player1['first_name']} {self.player1['last_name']} VS "
                f"{self.player2['first_name']} {self.player2['last_name']}")
