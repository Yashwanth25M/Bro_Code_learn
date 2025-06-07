# (07:33:34)

# static methods: A method that belongs to class rather than any object from that class

# Instance method : best for operation on instance off class(object) 
# static method : best for utility function that do not need access to class 
# in static methods we only need acess class dont need to access a object

class employee:

    def __init__(self , name , designation):
        self.name = name
        self.designation = designation

    def get_info(self):#instance method
        return f"{self.name} = {self.designation}"
    
    @staticmethod
    def is_valid_designation(designation):#static method
        valid_designation = ["manager" , "cashier" , "cook"]
        return designation in valid_designation
    
Employee1 = employee("A" , "manager")
Employee2 = employee("B" , "cashier")
Employee3 = employee("C" , "cook")

print(Employee1.get_info())
print(Employee2.get_info())
print(Employee3.get_info())

print(employee.is_valid_designation("manager"))
print(employee.is_valid_designation("rocket scientist"))