userVal = int(input("Please enter a number: "))
"""factor = []
for i in range(2,10,1):
    if(userVal % i == 0):
        list.append(factor,i)

if(len(factor)== 0):
    print("There is no factors between 2 and 10")
else:
    print(f"The factors are: {factor}")
    """    
    
factors = ""
for i in range(2,10,1):
    if(userVal % i == 0):
        factors+= (str(i) + ", ")
        
if(len(factors) == 0):
    print("The number has no factors between 2 and 10")
else:
    print(f"The factors of {userVal} between 2 and 10 are: {factors[0:-2]}")