from models.animal import Animal


class Dog(Animal):
    def __init__(self, nom) -> None:
        super().__init__(nom)

    def aboie(self):
        print("wouaf")