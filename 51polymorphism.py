# (07:21:10)

# polymorphism:Many forms

# class shape:
#     def area(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         print( self.radius * 3.14)

# class square(shape):
#     def __init__(self,side):
#         self.side = side

#     def area(self):
#         print(self.side ** 2)

# class Pizza(circle):
#         def __init__( self , toppings , radius):
#             super().__init__(radius)
#             self.toppings = toppings
            

# ######Circle1 = circle() #Circle1 is also circle ,also a shape but  not sqare 
# ######Square1 = square() #Square1 is also square ,also a shape but  not circle

# shapes = [circle(4) , square(5) , Pizza(toppings="pepperoni" ,radius= 15)]

# for Shape in shapes:
#     Shape.area()
