from Animal.animal import Animal


class Pets(Animal):
    def __init__(self, name, birth_date, sound, breed):
        super().__init__(name, birth_date, sound)
        self.breed = breed
        self.commands = []

    def set_breed(self, breed):
        self.breed = breed

    def get_breed(self):
        return self.breed

    def add_command(self, command):
        self.commands.append(command)

    def list_commands(self):
        return self.commands
