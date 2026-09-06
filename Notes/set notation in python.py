
'''
                                    Sets

- elements in a set can only be distinct, there can't be any duplicates at all
    - this is useful to getting rid of duplicates in a list
- sets are mutable
- always arranged in ascending order
- you can use set() to convert a list or tuple into a set



                                in and not in keywords
- used to check if values are in a set or not 

ex.

set1 = {1,2,3}
    if 3 in set1:
        print("3 is an element in the set")
    elif 6 not in set1:
        print("6 is not an element in the set")



                                discard and remove
- both have same purpose, to remove an element from the set
- difference is that .remove() will raise an error but .discard() will not

    
                                Set operators

- and is represented by &
- or is represented by |
- set difference is represented b -
    - however you can also use the .difference() function as well 
    
    
                            subset and super set check
                            
ex:
    
    set1 = {1,2,3}
    set2 = {2,3}
    
    subsetCheck = set2.issubset(set1) #output: True
    superCheck = set1.issuperset(set2) #output: True
    
    
    
'''


setA = {1, 2, 3}
setB = {2, 3, 4}
setC = set((1, 2, 3))
print(setA & setB)  # set intersection
print(setA | setB)  # set union
print(setA - setB)  # set difference
print(setC)

print(setA.add(4))
