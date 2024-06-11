from Animal.pets import Pets


class Dog(Pets):
    def __init__(self, name, birth_date, breed):
        super().__init__(name, birth_date, "Гав гав", breed)
        self.commands.extend(["сидеть", "лежать", "взять"])
