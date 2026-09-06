print("This will print a value to console")
type(12) #this returns variable type 
"""
Math operators: + - * /
Unique Operators: Mod, Exponential, Floor Division
    
- Mod (returns remainder): %

- Exponential: **

- Floor Division (integer division whereby it divides a number by another number 
where the quotient is a whole number rounded down): // 

- Mixing integer and float values will result in an answer that is float

*To use math functions you need to "import math"
"""

#Example 1 - reading user input, math operators, print to console
"""
sumOfMarks = float(input("What is the total number of marks? "))
marksAchieved = float(input("What is total amount of marks achieved? "))

percentageAchieved = marksAchieved / sumOfMarks *100

print("The percentage achieved is", round(percentageAchieved))
"""

#Example 2 - Artihmetic operations, print to console, assinging variables

a = 5 
b = 3 
c = 4 
d = 2

totalSum = ((a**2 + 3*c - d)/(a + (b - c)) * (d**2 % a)) / (b // d) 

#you use "," when theres different types. when theres only string, use "+"
print(totalSum, "hello")  

print(round(totalSum))

x= 12.3
print(float(int(x)))