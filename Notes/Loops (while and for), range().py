"""
                                            WHILE LOOP

while loop also has no curly brackets and also needs colon and indent
same format to if statement

while(condition):
    print()

you can also not use brackets for condition

while condition:
    print()
while loop example

num = 1
while (num < 10):
    
    print("Hello", num)
    num+=2
    


                                        for loop 

for targetVar in iterableObject:
    loop code
    
- you can use strings as a loop value

example

for i in "cat":
    print(i)


- To access the index of a list through a loop you can use enumerate

example

myList = [1,2,3]

for index, item in enumerate(myList):
    print(f"Index:{index}, value: {item}")

                                     For Loop ZIP

* zip makes lists of values of many lists together based on the index value

example 

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
list3 = [10, 20, 30]

for item in zip(list1, list2, list3):
print(item)

# Output:
# (1, 'a', 10)
# (2, 'b', 20)
# (3, 'c', 30)

** note that if a list is an index short compared to other lists, it wont make
a list for that index and instead will not print.

so if list3 = [10,20]

then it would only print (1, 'a', 10) and (2, 'b', 20)


                            break and continue

break ends the loop
continue skips everything in the current iteration below the keyword and goes 
to the next iteration

                                nested loops 
you nest for loops and they iterate whatever is in it before moving to the outer
loop



                                range() function

you can also create a range of numbers to start and/or stop using: 
    
- range(stop) for one argument which is excludes stop value
 
range(start, stop) for 2 arguments which is inclusive of start and exclusive
of stop

- range(start, stop, increment) allows you to have a value to increment by

*note to print a set of range you need to do print(*range()) using one of 
the 3 methods shown above

without the asterisk the console will print whatever it sees directly



                            Combining for loop and range()

for i in range(1, 10, 3):
    print(i)

using char in for loop example

digit = "012345678901234567890"
count0 = 0
count1 = 0
count2 = 0
for char in digit:
    if char == '0':
        count0 += 1
    elif char == '1':
        count1 += 1
    elif char == '2':
        count2 += 1
print(count0, count1, count2)
    

- to print values of a list 

my_list = [1, 2, 3]
for i in range(len(my_list)):
print(my_list[i])


- you dont need a loop to use range function

examples

- finding a sum

print(sum(range(1,3))) # prints 3


- num in range 

num = 7
if num in range(1, 11):
print(f"{num} is in the range.")
else:
print(f"{num} is not in the range.")



"""
myList = [1, 3, 3]

for index, item in enumerate(myList):
    print(f"Index:{index}, value: {item}")
