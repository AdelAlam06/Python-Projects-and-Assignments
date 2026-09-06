
import math

# author: Adel Alam

# Question 1 - reading user temperature in Celsius, returning in Kelvin & Farenheit

cTemp = float(input("Please enter a temperature in celsius: "))

kTemp = cTemp + 273.15

fTemp = cTemp * (9/5) + 32

print("Your temperature in farenheit is: ", round(fTemp, 1), "F")
print("Your temperature in kelvin is: ", round(kTemp, 1), "K")

# Question 2 - Quadratic formula calculator

print("The format of the standard equation of a quadratic function is: Ax^2 + Bx + C = 0")
a = float(input("Please enter your \"A\" value: "))
b = float(input("Please enter your \"B\" value: "))
c = float(input("Please enter your \"C\" value: "))

if (a == 0):
    print("Please enter a non zero \"A\" value")
elif (b**2 - 4*a*c < 0):
    print("There is no real root (graph does not touch the x-axis)")
else:
    x = (-b + math.sqrt(b**2 - 4*a*c)) / (2 * a)
    y = (-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)
    print("The roots of this function is:", round(x, 2), "and", round(y, 2))


# Question 3 - Checking to see if a triangle can be made with 3 user inputs

side1 = float(input("Enter a side length: "))
side2 = float(input("Enter a second side length: "))
side3 = float(input("Enter a third side length: "))

triangleCheck = side1 + side2 > side3 and side1 + \
    side3 > side2 and side2 + side3 > side1

print(triangleCheck)


# Question 4 - Area of a pentagon calculator

userLength = float(input("Please enter a side length of your pentagon: "))

area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))))/4 * (userLength**2)

print("The area of the pentagon is ", round(area, 2))


# Question 5 - solving for the nth Fibonacci number using an equation

gRatio = (1 + math.sqrt(5))/2

nTerm = int(input("Enter a term number in the fibonacci sequence: "))

termVal = (2 + gRatio)/5 * (gRatio**nTerm) + \
    (3 - gRatio)/5 * (gRatio**(-nTerm))

print("The term value is: ", round(termVal))
