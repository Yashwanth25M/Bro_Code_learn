# (07:39:31)

# class methods
# best for class-level data that  need access to class itself
# in below "count" is used within the class so class method(cls) is used

class student:

    count = 0

    def __init__(self , name , usn):
        self.name = name
        self.usn = usn
        student.count += 1

    # instance method
    def get_info(self):
        return f"{self.name} : {self.usn}"
    
    # class method
    # INSTEAD of using self use cls method
    @classmethod
    def get_count(cls):
        return f"Total number of student : {cls.count}"
    
student1 = student("A" , 1)
student2 = student("B" , 2)
student3 = student("C" , 3)
student4 = student("D" , 4)

print(student.get_count())