from datetime import date

from Animal.PackAnimals.camel import Camel
from Animal.PackAnimals.donkey import Donkey
from Animal.PackAnimals.horse import Horse
from Animal.Pets.cat import Cat
from Animal.Pets.dog import Dog
from Animal.Pets.hamster import Hamster
from Animal.animal import Animal


class AnimalRegistry:
    def __init__(self):
        self.registry = []

    def add_animal(self, animal):
        self.registry.append(animal)

    def list_commands(self, animal_name):
        for animal in self.registry:
            if animal.name == animal_name:
                return animal.list_commands()
        return []

    def teach_command(self, animal_name, command):
        for animal in self.registry:
            if animal.name == animal_name:
                animal.add_command(command)
                return True
        return False

    def list_animals_by_birth_date(self):
        return sorted(self.registry, key=lambda x: x.birth_date)

    @staticmethod
    def get_animal_count():
        return Animal.animal_count

    def make_sound(self, animal_name):
        for animal in self.registry:
            if animal.name == animal_name:
                return animal.make_sound()
        return "Такого животного нет."

    def display_menu(self):
        while True:
            print("\n Список доступных команд")
            print("\n1. Добавить животное в реестр")
            print("2. Показать команды которым обучено животное")
            print("3. Обучить животное новой команде")
            print("4. Показать дату рождения животных")
            print("5. Показать количество животных в реестре")
            print("6. Животное издает звук")
            print("7. Выход")
            choice = input("Введите команду: ")

            if choice == '1':
                self.add_animal_menu()
            elif choice == '2':
                self.list_commands_menu()
            elif choice == '3':
                self.teach_command_menu()
            elif choice == '4':
                self.list_animals_by_birth_date_menu()
            elif choice == '5':
                print(f"Всего в реестре числится: {self.get_animal_count()}")
            elif choice == '6':
                self.make_sound_menu()
            elif choice == '7':
                break
            else:
                print("Неверная команда, повторите ввод согласно списка доступных команд.")

    def add_animal_menu(self):
        animal_type = input("Введите животное (без отступов и пробелов) (собака, кошка, хомяк, лошадь, верблюд, "
                            "осел): ").lower()
        name = input("Введите кличку: ").lower()
        try:
            birth_date = date.fromisoformat(input("Введите дату рождения животного (YYYY-MM-DD): "))
        except ValueError:
            print("Неверный формат повторите ввод в таком YYYY-MM-DD формате.")
            return

        if animal_type == 'собака':
            breed = input("Введите породу: ").lower()
            animal = Dog(name, birth_date, breed)
        elif animal_type == 'кошка':
            breed = input("Введите породу: ").lower()
            animal = Cat(name, birth_date, breed)
        elif animal_type == 'хомяк':
            breed = input("Введите породу: ").lower()
            animal = Hamster(name, birth_date, breed)
        elif animal_type == 'лошадь':
            try:
                speed = float(input("Введите скорость в км.ч (0.0): "))
            except ValueError:
                print("Неверный формат, повторите ввод в формате (0.0).")
                return
            animal = Horse(name, birth_date, speed)
        elif animal_type == 'верблюд':
            try:
                humps = int(input("Введите количество горбов (от 1 до 2): "))
            except ValueError:
                print("Неверный формат, число должно быть целое.")
                return
            animal = Camel(name, birth_date, humps)
        elif animal_type == 'осел':
            try:
                stubbornness = int(input("Введите уровень его упрямства (1-покладистый - 10-непокорный): "))
            except ValueError:
                print("Неверный формат, число должно быть целое.")
                return
            animal = Donkey(name, birth_date, stubbornness)
        else:
            print("Либо при вводе введен отступ или пробел, либо это не домашнее животное (список указан при вводе).")
            return

        self.add_animal(animal)
        print(f"{animal_type.capitalize()} кличка {name.capitalize()} внесено в регистр.")

    def list_commands_menu(self):
        name = input("Введите кличку: ").lower()
        commands = self.list_commands(name)
        if commands:
            print(f"Животное {name.capitalize()} знает команды: {', '.join(commands)}")
        else:
            print("Это животное ещё не обучено.")

    def teach_command_menu(self):
        name = input("Введите кличку: ").lower()
        command = input("Какой команде хотите научить: ")
        if self.teach_command(name, command):
            print(f"{name.capitalize()} запомнила эту'{command}'.")
        else:
            print("Нет такого животного в реестре.")

    def list_animals_by_birth_date_menu(self):
        animals = self.list_animals_by_birth_date()
        for animal in animals:
            print(animal)

    def make_sound_menu(self):
        name = input("Введите кличку: ").lower()
        sound = self.make_sound(name)
        print(f"{name.capitalize()} говорит: {sound}")
