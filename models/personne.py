from models.animal import Animal


class Personne:
    def __init__(self,nom,personne) -> None:
        self.nom= nom
        self.personne = personne
        self.animaux = []

    def aj_ani(self,animal : Animal):
        self.animaux.append(animal)