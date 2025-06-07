# # (07:08:04)

# # super()
# # Function used in child class to call methods from parent class (super class)

class Shape:
    def __init__(self , color , filled  ) :
        self.color = color
        self.filled = filled
    def area(self):
        print("Calculate area")
        #The same function is also present in child classes
        #Child class override this method ,by riding their own
        # By utilizing super() methpod we can ride this method

class Circle(Shape):
    def __init__(self , color , filled ,radius ) :
        super().__init__(color , filled)
        self.radius = radius

    def area(self):
        super().area()
        print(f"The area of Circle is {self.radius * self.radius * 3.14}")

class Square(Shape):
    def __init__(self , color , filled ,width ) :
        super().__init__(color , filled)
        self.width = width

    def area(self):
        super().area()
        print(f"The area of Sqare is {self.width * self.width }")

class Triangle(Shape):
    def __init__(self , color , filled ,width  , heigth) :
        super().__init__(color , filled)
        self.width = width
        self.height = heigth

    def area(self):
        super().area()
        print(f"The area of Sqare is {self.width * self.height * 0.5 }")

print("Circle")
circle = Circle(color="Red" ,filled= True ,radius= 5)
print("color:",circle.color) 
print("is filled :",circle.filled) 
print("Radius:",circle.radius,"cm ")
circle.area()
print("\n")

print("Square")
square = Square("Blue" , False , 10)
print("color:",square.color) 
print("is filled :",square.filled) 
print("width:",square.width,"cm ")
square.area()
print("\n")

print("Triangle")
triangle = Triangle("Grey" , True ,5 , 10)
print("color:",triangle.color) 
print("is filled :",triangle.filled) 
print("Height :",triangle.height,"cm")
print("width :",triangle.width,"cm")
triangle.area()