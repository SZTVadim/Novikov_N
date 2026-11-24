# ЧАСТЬ 1
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


# ЧАСТЬ 2
class Dog(Animal):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


# ЧАСТЬ 3
class Zoo:

    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_animals(self):
        return self.__animals


# ЧАСТЬ 4
def animal_sound(animal):
    animal.make_sound()
# Это пример полиморфизма потому, что один вызов функции может сработать по-разному
# Если мы передаем собаку (dog) - то будет Гав-гав!, если кошку (cat) - Мяу!


dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)
zoo = Zoo("Городской зоопарк")
zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)
print(zoo.get_animals_count())
for animal in zoo.get_animals():
    animal_sound(animal)
# animal = Animal()
# Создать объект напрямую не получится, потому что это абстрактный класс
# И он содержит абстрактный метод make_sound(), который не реализован
# TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'
