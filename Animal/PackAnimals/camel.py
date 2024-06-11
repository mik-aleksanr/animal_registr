from Animal.packAnimals import PackAnimals


class Camel(PackAnimals):
    def __init__(self, name, birth_date, humps):
        super().__init__(name, birth_date, "Ыыы")
        self.humps = humps if humps <= 2 else 2
        self.commands.extend(["иди", "стой"])

    def set_humps(self, humps):
        self.humps = humps if humps <= 2 else 2

    def get_humps(self):
        return self.humps
