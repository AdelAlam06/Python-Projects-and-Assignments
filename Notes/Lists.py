"""
                                    Creating a list

- listExample = []

- converting a sequence to a list by using keyword: list()

- lists can contain various types of elements, not necessarily having to contain
one type of element only

- Indexing, slicing, repetition, length, membership check and sorting are the 
same as tuples 


                            Adding elements to a list

- .append(value) will add the value to the list at the end of the list

- .insert(index#, value) will add a value to the index number. It will increase
the index value of everything else by 1

- .extend(another list) will combine with another list 

                                Example to cover all ways
                                
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # Output: [1, 2, 3, 4]

my_list.insert(1, 5) # Insert 5 at index 1
print(my_list) # Output: [1, 5, 2, 3, 4]

another_list = [6, 7]
my_list.extend(another_list)
print(my_list) # Output: [1, 5, 2, 3, 4, 6, 7]


                            Removing elements in a list
                            
- .remove(value) will remove the first occurence of the element 

- .pop(index) will remove and return the value at the index provided 

- .pop() will remove and return the last item in the list

- .clear() will remove everything in a list

- del is a keyword that will remove the value at a given index in a list and shrink
the list by 1 index

                            Example to cover all ways
                            
my_list = [1, 2, 3, 2, 4, 5]
my_list.remove(2) # Remove the first occurrence of 2
print(my_list) # Output: [1, 3, 2, 4, 5]

popped_item = my_list.pop(1) # Remove and return item at index 1
print(f"my_list: {my_list}, popped_item: {popped_item}")
# Output: my_list: [1, 2, 4, 5], popped_item: 3

popped_item = my_list.pop() # Remove and return last item
print(f"my_list: {my_list}, popped_item: {popped_item}")
# Output: my_list: [1, 2, 4], popped_item: 5

del my_list[1] # Remove item at index 1
print(my_list) # Output: [1, 4]

my_list.clear() # Removes all items
print(my_list) # Output: []


                                Zip Function
                                
- a different way to merge lists

                                Example

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
zipped_list = list(zip(list_1, list_2))
print(zipped_list) # Output:[(1, 4), (2, 5), (3, 6)]

- if the two lists are not of equal size, it will only go up to the same index.
If list 1 has 2 indexes but list 2 has 3 indexes, zip will only make a list up
to the second index 
             
                               Comparisons
                               
- if comparing a list to a tuple it will return False, due to them being 
different types, regardless of them having the same elements

                            
                            Shallow and Deep copy
                      
- a shallow copy is a copy of a list that will change with whatever is added 
to the original list

- a deep copy is a copy of a list that will remain unchanged with whatver is added
to the original list
                            
import copy
original_list = [1, [2, 3], [4, 5]]

shallow_copy = copy.copy(original_list)
deep_copy = copy.deepcopy(original_list)

original_list[1][0] = 7

print(original_list) # Output: [1, [7, 3], [4, 5]]
print(shallow_copy) # Output: [1, [7, 3], [4, 5]]
print(deep_copy) # Output: [1, [2, 3], [4, 5]]


                             List Comprehension

- creating a list using conditionals and loops

- format: [<expression> for <elem> in <sequence> if <test>]


                                Example

cubes = [x**3 for x in range(6) if x % 2 == 0]
print (cubes)


                        Nested List Comprehension

example 

matrix = [[1,2,,3], [4,5,6], [7,8,9]]

flattened = [num for row in matrix for num in row]

print (flattened)

                        Combining multiple types
                    
names = ["Alice", "Bob", "Charlie" ]
ages = [25,30,35]
nameAgePairs = [(name +"A.", age + 1) for name, age in zip(names, ages)]
print(nameAgePairs)

                            Harder example
                            
#all returns TRUE if all of the items of a passed iterable (List, Dictionary, 
Tuple, Set, etc.) are True; otherwise, it returns FALSE 

primes = [x for x in range(2,20) if all(x%y != 0 for y in range(3,x))] 

unflattened:
    primes = []
    for x in range(2,20):
        for y in range(3,x):
            if (x%y!= 0):
                continue
            else:
                primes.append[x]

print (primes) #[2, 3, 4, 5, 7, 11, 13, 17, 19]

"""
