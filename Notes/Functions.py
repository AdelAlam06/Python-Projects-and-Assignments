"""
- to create/define a function you need keywrod def

naming convention for functions is camel notation


                            example of declaration

def firstLast (firstName, lastName):
    print(firstname + " " + lastName)




- to call a function use it's name and input proper values

                continuation of prior example

firstLast("Adel", "ALam")


you can also return a value when it is called

                                example

def firstLast (firstName, lastName):
    fullName = firstname + " " + lastName
    return fullName

returnedName = firstLast("Adel", "Alam")
print(returnedName)



                            Default Parameters
- you can set default parameters in case the user does not input their own values

- these parameters can change the type of the variable the value is going into

Two ways to have default parameters:
    1. give default parameters to all variables
    2. if you need a select amount of default parameter then have all the 
    variables that require a default parameter on the right side while non-default
    parameters remain on the left side.
    
                            Example for choice 1
def addNum(num1 = 100, num2 = 1000, num3 = 1):
    return num1+num2+num3
                            

                            Example for choice 2
def addNum(num1, num2 = 1000, num3 = 1): 
    return num1+num2+num3

- you can also declare variables directly from the calling function, so you can
change the order in which the variables will go into.

                            Example
                            
def addNum(num1, num2 = 1000): 
    return num1+num2    

addNum(num1 = 1, num2 = 10)
addNum(1)


                                    Note on None

- if you return nothing or have no return statement then it returns None by default

- to check if a variable is None use the statement: var is None with is None being
keywords and var being the variable you're checking

Three ways to return None:
    1. write no return statement since it returns by default (best option)
    2. write just return
    3. write return None


                                   Returning Tuples
                                    
- tuples allow you to return multiple values at once, however you will also
need multiple variables to hold the returning values as well


                                    Example
                                    
def get_circle_properties(radius):

    area = 3.14159 * radius**2
    circumference = 2 * 3.14159 * radius
    return area, circumference

circle_area, circle_circumference = get_circle_properties(5)
print(f"Circle Area: {circle_area}")
print(f"Circle Circumference: {circle_circumference}")


                                Global and Local

- local variables are limited to the functions they're located in and cannot 
be used outside a given scope

- global variables can be accessed anywhere and they have to be written at the 
top of programs or above functions that will be using it

- to change a global variable use keyword: global

                                Example

z = 30 # This is a global variable
def my_function():
    
    # Declare that we want to use the global z variable
    global z

    z = 40 # This modifies the global z variable
    print(f"Inside the function: {z}")
    
print(f"Before the function is invoked: {z}")
my_function()
# Now, z has been modified globally
print(f"Outside the function: {z}")

"""
