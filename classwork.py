# #EXAMPLE 1 (conversion from upper to loower case)
name1= "RAHUl"
name2= "SHJHSSHI"
name3= name1.lower()
print(name3)

# #EXAMPLE 2 (addition of string)
name4= name1 +" "+ name2
print(name4) 

# #example3 (boolean value output(true or false))
a = 48
b=67
print(a<b)

#INPUT EXAMPLE
salary=(input("enter your number\t"))
print(salary)
print(type(salary))

#FINDING THE LARGEST AMONG TWO
a= int(input("Enter the first number"))
b = int(input("Enter the  second number"))
if(a>b):
    print("a is the greatest")
else:
    print("b is greatest")

# #Example6
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if a>b: 
    print("a is greater than b.")
else:
    print("b is greater than a.")
    
# #Example7M( ODD OR EVEN)
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# #Example8 (POSITIVE NEGATIVE)
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
# #Example9 (LEAP YEAR OR NOT)
year = int(input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# #Example 
n = 5
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

# #Example12
import math
print("Factorial of 5:", math.factorial(5))

# #Example13 (TABLE OF 5)
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# #Example14 (NUMBER FROM 1 TO 10)
for i in range(1, 11):
    print(i, end=" ")

#GRADE PROGRAM USING IF ELIF
marks= int(input("enter the marks\n"))
if(marks>90 and marks<=100):
    print("GRADE A")
elif(marks>80 and marks<=90):
    print("GRADE B")
elif(marks>70 and marks<=80):
    print("GRADE C")
else:
    print("GRADE D")