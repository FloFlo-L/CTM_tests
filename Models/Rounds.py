import json


class Round:
    def __init__(self, round_number, round_name, matches):
        """
        Initialise une nouvelle instance de la classe Round.

        Args:
            round_number (int): Le numéro du tour.
            round_name (str): Le nom du tour.
            matches (list): Liste des matches pour ce tour.
        """
        self.round_number = round_number
        self.round_name = round_name
        self.matches = matches

    def serialize(self):
        """
        Sérialise l'objet Round pour la sauvegarde sous forme de dictionnaire.

        Returns:
            dict: Représentation sérialisée de l'objet Round.
        """
        return {
            'round_number': self.round_number,
            'round_name': self.round_name,
            'matches': [match.serialize() for match in self.matches]
        }

    def save_round(self, tournament_id):
        """
        Sauvegarde l'objet Round dans le fichier JSON des tournois.

        Args:
            tournament_id (int): L'ID du tournoi auquel ce tour appartient.

        Note:
            Cette méthode met à jour le fichier tournaments.json en ajoutant le round au tournoi spécifié.
        """
        new_round = self.__dict__
        with open('data/tournaments.json', 'r+') as file:
            tournaments = json.load(file)
            for tournament in tournaments:
                if tournament['id'] == tournament_id:
                    if 'round_list' not in tournament:
                        tournament['round_list'] = []
                    tournament['round_list'].append(new_round)
                    break
            file.seek(0)
            file.truncate()
            json.dump(tournaments, file, indent=4)
