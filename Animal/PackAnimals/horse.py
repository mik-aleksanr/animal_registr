from Animal.packAnimals import PackAnimals


class Horse(PackAnimals):
    def __init__(self, name, birth_date, speed):
        super().__init__(name, birth_date, "Иго го")
        self.speed = speed
        self.commands.extend(["иди", "беги", "стой"])

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed
