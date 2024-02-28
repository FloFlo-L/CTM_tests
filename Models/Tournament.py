import os
import json
from Models.Model import Model


class Tournament(Model):
    def __init__(self, name, location, start_date, end_date, rounds=4, current_round=1,
                 round_list=[], player_list=[], description=""):
        """
        Initialise une nouvelle instance de la classe Tournament.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
            start_date (str): Date de début du tournoi.
            end_date (str): Date de fin du tournoi.
            rounds (int, optional): Nombre total de tours dans le tournoi. Par défaut à 4.
            current_round (int, optional): Le tour actuel du tournoi. Par défaut à 1.
            round_list (list, optional): Liste des tours du tournoi. Par défaut vide.
            player_list (list, optional): Liste des joueurs du tournoi. Par défaut vide.
            description (str, optional): Description du tournoi. Par défaut vide.
        """
        self.id = self.get_new_id('data/tournaments.json')
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.current_round = current_round
        self.round_list = round_list
        self.player_list = player_list
        self.description = description

    def save_tournament(self):
        """
            Sauvegarde l'objet Tournament dans le fichier JSON des tournois.
        """
        new_tournament = self.__dict__

        # S'assurer que le dossier 'data' existe
        if not os.path.exists('data'):
            os.makedirs('data')

        # Créer le chemin du fichier avec le nom du tournoi
        file_path = 'data/tournaments.json'

        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump([new_tournament], file, indent=4)
        else:
            with open(file_path, 'r+') as file:
                existing_tournaments = json.load(file)
                existing_tournaments.append(new_tournament)
                file.seek(0)
                file.truncate()
                json.dump(existing_tournaments, file, indent=4)

    def get_tournaments(self):
        """
        Récupère la liste de tous les tournois à partir du fichier JSON des tournois.

        Returns:
            list: Liste des tournois.
            ou
            str: Message d'erreur si le fichier n'existe pas.

        Note:
            Si le fichier tournaments.json n'existe pas, cette méthode retourne un message d'erreur.
        """
        file_path = 'data/tournaments.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                tournaments = json.load(file)
                return tournaments
        else:
            return print('Le fichier tournaments.json est introuvable')

    def update_tournament(self, updated_tournament):
        """
        Met à jour un tournoi spécifique dans le fichier JSON des tournois.

        Args:
            updated_tournament (dict): Le tournoi mis à jour.

        Note:
            Recherche le tournoi à mettre à jour en utilisant son ID, puis le remplace
            par la version mise à jour dans le fichier tournaments.json.
        """
        if os.path.exists('data/tournaments.json'):
            with open('data/tournaments.json', 'r') as file:
                tournaments = json.load(file)
            for i, tournament in enumerate(tournaments):
                # On utilise maintenant l'ID pour vérifier le bon tournoi
                if tournament['id'] == updated_tournament['id']:
                    tournaments[i] = updated_tournament
                    break
            else:
                print("Tournoi introuvable")
                return

            with open('data/tournaments.json', 'w') as file:
                json.dump(tournaments, file, indent=4)
        else:
            print('Fichier tournaments.json introuvable')
