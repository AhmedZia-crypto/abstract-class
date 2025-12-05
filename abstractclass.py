from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def mileage(self):
        pass

class Bike(Vehicle):
    def mileage(self):
        print("Hello")

class Car(Vehicle):
    def mileage(self):
        print("How are you")

obj1 = Bike()
obj1.mileage()

obj2 = Car()
obj2.mileage()