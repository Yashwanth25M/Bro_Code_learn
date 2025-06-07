# (07:29:15) 

# duck typing
# Another way to achive polymorphism
# If it looks like a duck and  quacks like a duck , it must be duck

class Animal:
    alive = True

class dog(Animal):
    def speak(self):
        print("BOW!!")

class cat(Animal):
    def speak(self):
        print("MEOW!!")

class car :
    #car looks like a animal , speaks like animal then its also a animal
    alive = False
    def speak(self):
        print("HONK!!")

animals = [ dog() , cat() , car() ]
for animal in animals:
    animal.speak()
    print(animal.alive)