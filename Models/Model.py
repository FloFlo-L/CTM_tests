import json
import os


class Model:
    def get_new_id(self, data_file_path):
        """
        Récupère un nouvel ID unique basé sur le dernier ID dans le fichier JSON spécifié.
        Si le fichier n'existe pas ou est vide, retourne 1.

        Args:
            data_file_path (str): Chemin d'accès au fichier JSON contenant les données.

        Returns:
            int: Le nouvel ID unique.
        """
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as file:
                data = json.load(file)
                if data:
                    last_id = data[-1].get('id', 0)
                    return last_id + 1
                else:
                    return 1
        else:
            return 1
