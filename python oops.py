# Python polymorphism
# class Cat:
#      def sound(self):
#         print("Meow")
#
# class Fox:
#     def sound(self):
#         print("Wa-pa-pa-pa-pa-pow!")
#
# c1 = Cat()
# f1 = Fox()
# c1.sound()
# f1.sound()


# Python inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(self.name)
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def number(self):
#         super().speak()
#         print(self.age)
#
# a1 = Animal("rex")
# d1 = Dog("robin", 2)
# d1.number()
# a1.speak()

#__init__() method
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(self.name, "says Woof!")
#
# d1 = Dog("Buddy", 3)
# d1.bark()


#Python classes/objects
# class Person:
#     def __init__(self, name, age):
#         self.person = name
#         self.age = age
#
#     def greet(self):
#         print("Hello, my name is", self.person, "and age is", self.age)
#
# p1 = Person("John", 36)
# p1.greet()


#Python encapsulation
# class ScoreBoard:
#     def __init__(self, score):
#         self.__mark = score
#
#     def get_score(self):
#         return self.__mark
#
# s1 = ScoreBoard(20)
# print(s1.get_score())


# class Man:
#     def __init__(self, name):
#         self.name = name
#
#     def entry(self):
#         print("my name is", self.name)
#
# class Number:
#     def __init__(self, age):
#         self.age = age
#
#     def entry(self):
#         print("my age is", self.age)
#
# m1 = Man("John")
# n1 = Number(25)
# m1.entry()
# n1.entry()

#Python abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.first = side1
        self.second = side2
        self.third = side3

    def area(self):
        return int(1/2 * self.base * self.height)

    def perimeter(self):
        return self.first + self.second + self.third

t1 = Triangle(25, 30, 2, 5, 6)
print(t1.area())
print(t1.perimeter())
