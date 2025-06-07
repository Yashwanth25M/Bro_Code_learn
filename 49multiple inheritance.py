# (07:00:02) 

# multiple inheritance
# inhherit from more than one parent class { C(A,B)}

# multi-level inherutence
# nherit from a parent which inherits from another parent {  C(B) <- B(A) <- A }

class Animal:

    def __init__(self , name):
        self.name = name

    def eat(self):
        print(f"{self.name} animal is eating")
    
    def sleep(self):
        print(f"{self.name} aniimal is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} animal is fleeing")

class predator(Animal):
    def hunt(self):
        print(f"{self.name} animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(predator):
    pass

class Fish(Prey , predator):
    pass 

##### CLASS FISH INHERITS FROM BOTH Prey AND predator CLASS WHICH IS MULTIPLE INHERITANCE
##### CLASS Prey AND predator INHERITS FROM ANIMAL , WHICH IS HERITED BY CLASS Rabbit ,Hawk , Fish which is multi-level inheritence

print("Rabbit")
rabbit = Rabbit("raabit")
rabbit.flee()
rabbit.eat()
rabbit.sleep()

print("Hawk")
hawk = Hawk("howk")
hawk.hunt()
hawk.eat()
hawk.sleep()

print("Fish")
fish = Fish("fosh")
fish.flee()
fish.hunt()
fish.eat()
fish.sleep()