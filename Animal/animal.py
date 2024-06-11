class Animal:
    animal_count = 0

    def __init__(self, name, birth_date, sound):
        self.name = name
        self.birth_date = birth_date
        self.sound = sound
        Animal.animal_count += 1

    def make_sound(self):
        return self.sound

    def __str__(self):
        return f"{self.name} ({self.birth_date}) - {self.make_sound()}"
