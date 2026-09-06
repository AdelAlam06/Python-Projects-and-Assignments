"""
Strings

Concatenation

- You can concatenate strings with other strings
- you CANNOT concatenate strings with numeric data types
- you need to convert numeric types to string first

Examples

- str1 = "Hello" + " World"
- str2 = " the cat meowed"
- str3 = str1 + str2
- print(str3 + str2 + str1)  
- str4 += str3

to convert to string just use str(data)

                            String output

to combine various types of data type with string you can use f string

example
name = "Adel"
age = 18
print(f"Hello {name}! You are {age} years old")

python has the same escape characters (for the most part) as C# and Java
\n,\t,\r,\', \", \""", \\, \b, etc.



                            Single Vs Double Quotation

You can use ' " " ' or " '' " depending on what is needed and they're both 
accepted ways of stating a string

For multiline string text use triple quotes

Example: username = *\""" Hello, line 1
                        line 2
                        line 3\"""
                        
*remove front slash for it to work


                                String Length
                                
String length in python is len(data) (all lowercase Len)
- escape characters are included in the length
example

str = "Hello World"
print(len(str))




                                Indexing

- python has 2 types of indexing, positive and negative

Example

Hello World!
Positive index would go 0-11 left to right 
Negative index would go -12 to -1 left to right

Example of reversed output

str1 = "Hello World"
for index in range(len(str1) -1, -1, -1):
    print(str1[index])




                            String iteration

2 ways of doing this, using range() function or just a string

with range you can have range(optional start, stop, optional step)

example 1 - with range()

str1 = "Hello World"
for index in range(1, str1, 2):
    print(str1[index])
    

example 2 - just plain string

str1 = "Hello World"
for index in str1:
    print(str1[index])
    
range() is better due to more flexibility of choosing what to print whereas
just plain string is only going to print what is in the string



                                    String slicing

- str[start:end:optional step] - slicing middle of the string with possible step
- str[:end] - slicing out from the end of a string
- str[start:] - slicing out from the start of a string

* the character at the start index is included and the character at the end 
index is excluded

examples without step

str1 = "Hello World"
print(str1[1:5]) <- this will only print ello

*note that indexing from an end can be anything, meaning:

str1 = "Hello"

str1[0:5] will be the same as str1[0:20]

examples with step

text = "Python Programming"

substring1 = text[::2] "Pto rgamn"
substring2 = text[::3] #"Ph oai"
substring3 = text[::20] #"P"




                            String methods

str1 = "Hello World!"
str1.isalpha() - checks if all the characters in the string are alphabetical
str1.isdigit() - checks if all the characters in the string are numeric
str1.upper() - converts all the characters in the string to uppercase
str1.lower() - converts all the characters in the string to lowercase

- there's way more but these are the more common ones


                            STRINGS CAN'T BE MODIFIED

modification is different from concatenation

Example

originalString = "Hello World! "

originalString = originalString + "How are you?" this is allowed

originalString[0] = "J" this is NOT allowed



                                end keyword
                                
this is to allow you to add anything at the end of a print statement

                                example
from time import sleep

print("Completed 0%", end="\r")
sleep(1) # pausing for 1 second so that we can see the changes
print("Completed 50%", end="\r")
sleep(1) # pausing for 1 second so that we can see the changes
print("Completed 100%", end="\r")

"""
