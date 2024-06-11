from Animal.pets import Pets


class Hamster(Pets):
    def __init__(self, name, birth_date, breed):
        super().__init__(name, birth_date, "Пи пи пи", breed)
