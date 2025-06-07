# (07:59:51)
 
# @property
# Decorator used to define a method as a property
# Benefit:Add additional logic when read , write or delete an attributes
# gives getter(read) , sette(write) , and deleter(delete) method

class Rectangle:

    def __init__(self , width , height):
        self._width = width   #by pre-fixing _ it becomes private attribute
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"#getter method

    @property
    def height(self):
        return f"{self._height:.1f}cm"#getter method
    
    @width.setter
    def width(self , new_width):
        if new_width > 0:
            print("Width  greater than zero")
            self._width = new_width
            print(new_width)
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self , new_height):
        if new_height > 0:
            print("height  greater than zero")
            self._height = new_height
            print(new_height)
        else:
            print("height must be greater than zero")
    
    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")

rectangle = Rectangle (3 , 4)

rectangle.width = 5
rectangle.height = 6

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height 