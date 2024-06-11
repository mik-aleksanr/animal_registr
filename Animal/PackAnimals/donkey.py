from Animal.packAnimals import PackAnimals


class Donkey(PackAnimals):
    def __init__(self, name, birth_date, stubbornness):
        super().__init__(name, birth_date, "И-а и-а")
        self.stubbornness = stubbornness
        self.commands.extend(["иди", "стой"])

    def set_stubbornness(self, stubbornness):
        self.stubbornness = stubbornness

    def get_stubbornness(self):
        return self.stubbornness
