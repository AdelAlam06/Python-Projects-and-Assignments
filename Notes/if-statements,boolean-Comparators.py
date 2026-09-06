#Boolean
#True and False has to be capitalized
trueVal = True
falseVal = False

"""
In python there are various ways a boolean can return True using bool()

bool() will return True if the value is:
    
- True
- a string (except empty string)
- any number except 0
- boolean comparators that evaulate to true
- any list, tuple, set, or dictionary except empty ones

bool() will return False if the value is:
    
- False
- boolean comparators that evaulate to false
- empty strings
- the number 0
- an empty list, tuple, set or dictionary
- the value None
"""

"""
if statements in python dont need curly brackets but they need a colon and
need to be indented under the if statement

Just if statement

if(condition):
    print("True")


Simple if else statement

if(condition):
    print("True")
else:
    print("False")
    
    
if/elif/else statement
    
if(condition1):
    print("True")
elif(condition2):
    print("True OR False")
elif(condition3):
    print("True AND False")
else:
    print("False")
"""

"""
Boolean operators

in OOP languages its &&,||,!

in Python it's and, or, not

"""
print(bool(True and False))
    
if("True" == True):
    print("it is true")

#using 0 or empty string empty set results in a false outcome
if(0 or "" or []):
    if(1):
        print("A")




