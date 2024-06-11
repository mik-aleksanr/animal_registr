from Animal.animal import Animal


class PackAnimals(Animal):
    def __init__(self, name, birth_date, sound):
        super().__init__(name, birth_date, sound)
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        return self.commands
