"""
Dictionary

- creating a dictionary


example

student = {
    "name": "Alice",
    "age": 25,
    "major": "Computer Science"
    }

print (student)

- on the left side of the colon is the "key" or the variable that can be 
used to index the value that is on the right side of the colon



example building on the last example

student_name = student["name"]
student_major = student["major"]

print("Student Name:", student_name) # Output: Student Name: Alice
print("Student Major:", student_major) # Output: Student Major: Computer Science


                                .get() function

- another way to index a dictionary
- it has a the format: .get(index, default value)


example building on first example

# Accessing elements using get() and providing a default value
# If default value is not provided it is set to None
student_name = student.get("name", "Name not found")
student_age = student.get("age", "Age not found")
student_major = student.get("major", "Major not found")

- if the get values are not found it will default to the statement "__ not found"
when printing it to console


                                    Order
                                    
- dictionary keys are first come first serve. Whatever is declared first remains
first


                                Mutability
                                
- dictionary VALUES can be changed 
- key's cannot be replaced, they can be removed and apply the value to another 
key

                            
                                Removing a key word
                                
- use del 

student = {
"name": "Alice",
"age": 25,
"major": "Computer Science",
}
# Removing a key from the dictionary
del student["age"]

** it will raise error if key that is being removed does not exist


                            Iterating a dictionary

- python automatically iterates the keys in a dictionary

student = {"name": "Alice", "major": "CS"}

for key in student:
    print(f"{key}: {student[key]")


- however if you want to iterate the values, you can do that as well

- you will need .values() at the end of a dictionary you want to iterate


example

student = {"name": "Alice", "major": "CS"}

for value in student.values():
    print(f"{value}")


                            List of dictionary
                            
students = [
{"name": "Alice", "age": 25, "major": "CS"},
{"name": "Bob", "age": 22, "major": "Math"},
{"name": "Charlie", "age": 24, "major": "Phys"},
]

# Iterating over the list of dictionaries

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")
# Output:
# Name: Alice, Age: 25, Major: CS
# Name: Bob, Age: 22, Major: Math
# Name: Charlie, Age: 24, Major: Phys



                                Map function
                                
- applies a function to every items in an iterable data type

- format is: .map(function_name, iterable_name)


                                Example
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]
# Define a custom function to double a number
def double(x):
return x * 2
# Use map to apply the double function
# to each element in the list.
# Call list() to trigger evaluation of map iterator
doubled_numbers = list(map(double, numbers))
print(doubled_numbers) # Output: [2, 4, 6, 8, 10]





"""
