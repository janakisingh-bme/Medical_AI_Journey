"""name="Janaki"
age=23
height=5.5
is_student=True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))"""
"""a=3
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)  
print(a%b)
print(a**b)
print(a//b)"""
"""age = 21

print(age > 18)
print(age < 18)
print(age == 21)
print(age != 21)
print(age >= 21)
print(age <= 21)"""
"""name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height: "))
print("Hello", name, "You are", age, "years old.")"""
"""age=int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")"""
"""marks = int(input("Enter your marks: "))

if marks >= 80:

    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")"""
"""for i in range(1,5):
    print(i)"""
count=1
"""while count <= 5:
    print(count)
    count += 1
"""
"""def greet():
    print("Hello! Welcome to the program.")
greet()"""#indentation error may come ,keep it in mind while writing code
"""import math

number = float(input("Enter a number: "))

print("Square root:", math.sqrt(number))"""
# Calculate Area of a Circle

import math

radius = float(input("Enter the radius: "))

area = math.pi * radius ** 2

print("Area of the circle:", round(area, 2))