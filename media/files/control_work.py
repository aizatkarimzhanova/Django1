class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def make_sound(self):
        print("Животное издает звук")

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age


class Dog(Animal):
    def make_sound(self):
        print("Собака: гаф гаф")

class Cat(Animal):
    def make_sound(self):
        print("Кошка: мяу мяу")

animal = Animal("Bembi", "5 month")
print(f"Name:{animal.get_name()}, age:{animal.get_age()}")
animal.make_sound()

dog = Dog("Bars", "2 year")
print(f"Dog:{dog.get_name()}, age:{dog.get_age()}")
dog.make_sound()
cat = Cat("Lili", "7 month")
print(f"Cat:{cat.get_name()}, age:{cat.get_age()}")
cat.make_sound()

dog.set_name("Rex")
dog.set_age("3 year")

print("После изменения через сеттеры:")
print(f"Dog: {dog.get_name()}, age: {dog.get_age()}")
