# (06:44:50)

# class variables

class student:

    class_year = 2024 #class variable
    num_students = 0

    def __init__(self , name , age):
        self.name = name
        self.age = age
        student.num_students += 1

S1 = student("ajay" , 12)
S2 = student("abhi" , 13)
S3 = student("BAla" , 14)
S4 = student("Bhima" , 14)

print(S1.name)
print(S1.age)
print(S1.class_year)
print(student.class_year)
print(student.num_students)

print(f"My graduating class of {student.class_year} has {student.num_students} students")
print(S1.name)
print(S2.name)
print(S3.name)
print(S4.name)