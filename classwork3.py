#file handling  (read, open, close)
# file=open("50 datas.txt","r")
# print(file.read())
# file.close()
#creat an empty class
# class Student:
#     pass 

#creat a class which has a value
# class Student:
#     def __init__(self, name, roll_num, age):
#         self.name = name
#         self.roll_num = roll_num
#         self.age= age
# s1= Student("xyz",208,23)
# s2= Student("abc",209,23)
# print(s1.name, s1.roll_num,s1.age)
# print(s2.name, s2.roll_num,s2.age)


#swapping two numbers using function
# def swapping(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
#     print(a,b)
# a=int(input("enter you number"))
# b=int(input("enter you number"))
# swapping(a,b)





# Parent Class (Base Class)

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_person(self):
#         print("Name :", self.name)
#         print("Age  :", self.age)


# Child Class (Derived Class)

# class Student(Person):

#     def __init__(self, name, age, roll_no, marks):
#         # Call Parent Constructor
#         super().__init__(name, age)

#         # Child Class Variables
#         self.roll_no = roll_no
#         self.marks = marks

#     def show_student(self):
#         print("Roll Number :", self.roll_no)
#         print("Marks       :", self.marks)

# Create Object
# student1 = Student("shiv prakash shukla", 20, 101, 92)
# # Display Data
# print("Student Information")
# print("--------------------")
# student1.show_person()      # Parent Class Method
# student1.show_student()     # Child Class Method
