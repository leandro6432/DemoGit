from models.animal import Animal


class Chat (Animal):
    def __init__(self, nom, griffe_coupe) -> None:
        super().__init__(nom)
        self.griffes_couper = griffe_coupe