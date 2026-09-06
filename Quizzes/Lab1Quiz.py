import math

numOfSides = float(input("Please enter the number of sides of your polygon: "))
sideLength = float(input("Please enter length of the side: "))

perimeter = sideLength*numOfSides

apothem = sideLength/(2 * math.tan(math.pi/numOfSides))

area = (perimeter * apothem)/2

print (f"The area is {round(area,2)}")