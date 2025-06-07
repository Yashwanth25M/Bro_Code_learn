# 06:53:06)

# inheritance
# Allows a class to inherit atributes and methods from another class

class animal:

    def __init__(self , name):
        self.name = name
        self.isalive = True

    def eat(self):
        print(f"{self.name} is eating .")

    def sleep(self):
        print(f"{self.name} is sleeping .")
    
class Dog(animal):
    def speak(self):
        print("woooh")

class Cat(animal):
    def speak(self):
        print("Meowww")

class Mouse(animal):
    def speak(self):
        print("Chiiichii")

dog = Dog("jackie")
cat = Cat("doodh_paglu")
mouse = Mouse("Chut")

dog.eat()
print(f"{dog.name} is alive : {dog.isalive}")
dog.sleep()
dog.speak()
cat.eat()
print(f"{cat.name} is alive : {cat.isalive}")
cat.sleep()
cat.speak()
mouse.eat()
print(f"{mouse.name} is alive : {mouse.isalive}")
mouse.sleep()
mouse.speak()