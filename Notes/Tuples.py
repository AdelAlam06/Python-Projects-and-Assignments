"""
                                            Tuples
                                            
tuples use () brackets

Examples 

emptyTuple = () #prints empty tuple

mixedTuple = (1,"apple", 2, "banana") #allows for using multiple data types

coordinates = (3.14, 2.71, 1.33)

myFruit = "cherry"

tupleFromVar = (1,myFruit)

print(tupleFromVar) #output: (1, 'cherry')


                                        Single Tuple
                                        
For a single tuple, you need trailing comma

Example

singleTuple = (42,) #it will print (42,)

singleTuple2 = (42) # it will print 42




                                    Nested Tuples
its possible to create nested tuples

Example

nestedTuple = ((1,2,3), ("a", "b", "c"), (True,False))


Accessing elements from prior example

print(nestedTuple[0]) #output: (1,2,3)
print(nestedTuple[1][2]) #output: c





                                    Tuple in function

def addAndSubtract(a,b):
    sumResult = a + b
    differenceResult = a-b
    
    return sumResult, diffResult #creates tuple

sumeResult,diffResult = addAndSubtract(1,2)

*brackets can be used however it is completely optional



                                    Ignoring Some values

use underscore for variables you want to skip

coordinates = (3.14, 2.71, 1.33)
x, _ ,z = coordinates

    

                                    Collecting Tuples

to collect remaining values into a single variable use asterisk *

coordinates = (3.14, 2.71, 1.33)

first, *rest = coordinates

print(first) #prints 3.14

print(rest) #prints a LIST of [2.71,1.33]


                    Converting an int list and string into a tuple
- use keyword tuple()
Creating a tuple from existing sequences

myString = "Hello"

tuple1 = tuple(myString)

print(tuple1) #splits the string into ('H', 'e', 'l', 'l', 'o')


my_list = [10, 20, 30] # we use square brackets to create a list
tuple_from_list = tuple(my_list)
print(tuple_from_list) # Output: (10, 20, 30)

                                    
                                        Indexing 

Indexing in a tuple is the same as in a string

negative starts from -1 and starts from end of an element

positive starts from 0 and starts from the start of an element

Example

my_tuple = (10, 20, 30, 40, 50)

element1 = my_tuple[0] # Access the first element
element1 = my_tuple[-5] # Access the first element as well

                                Indexing many tuples (slicing)
                                
myTuple = (10,20,30,40,50)

subset = myTuple [1:4] #slices to get elements at index 1, 2, 3
print (subset) #prints (20,30,40)


subset2 = myTuple [:2] #this will print (10, 20)

                              
                                    
                              Concatenation
                              
- tuples can be concatenated to create a bigger tuple

                                Example
tuple1 = (1, 2, 3)
tuple2 = (1, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple) # Output: (1, 2, 3, 4, 5, 6)


                                Repetition

- tuples can also be repeated 

                                Example
original_tuple = (1, 2)
repeated_tuple = original_tuple * 3
print(repeated_tuple) # Output: (1, 2, 1, 2, 1, 2)


                            Membership testing
- check if an element is present in a tuple using the "in" operator

                                Example
fruits = ("apple", "banana", "cherry")
print("banana" in fruits) # Output: True
print("grape" in fruits) # Output: False


                                Length
- use len()

                                Sorting

- keyword: sorted()                                
- this function returns a LIST not a TUPLE
- sorted least to greatest left to right

                                Example
my_tuple = (3, 1, 4, 1, 5, 9, 2)
sorted_list = sorted(my_tuple)
print(sorted_list) # Output: [1, 1, 2, 3, 4, 5, 9]


- you can use sort function to sort greatest to least as well
- keyword: sorted(tuple, reverse = True)

                                Example
my_tuple = (3, 1, 4, 1, 5, 9, 2)
sorted_list_reversed = sorted(my_tuple, reverse=True)
print(sorted_list_reversed) # Output: [9, 5, 4, 3, 2, 1, 1]


                            Count Function
                            
- allows you to count ALL occurences of an element
keyword: .count(element)

                               Example
my_tuple = (1, 2, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)
print(count_of_2) # Output: 4

                                Index Function

- finds the FIRST occurence (index) of the element it's looking for
- keyword: .index(element)

my_tuple = (10, 20, 30, 30, 40, 50)
index_of_first_30 = my_tuple.index(30)
print(index_of_first_30) # Output: 2
# (because first 30 is at index 2)


                                Immutability
                                
- values at given indexes cannot be changed but new values can be concatenated 
to the tuple, not appended

                                Example
                                
my_tuple = my_tuple + (4, 5)
print(my_tuple) # Output: (1, 2, 3, 4, 5)

# Attempt to change an element
# This will raise TypeError error
my_tuple[1] = 4






"""
