from Animal.pets import Pets


class Cat(Pets):
    def __init__(self, name, birth_date, breed):
        super().__init__(name, birth_date, "Мяу", breed)
