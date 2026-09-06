"""
                                Float Comparisons

not all float comparisons will work

examples

doesn't work
a = 0.1 + 0.2
b = 0.3

if(a==b):
    print("works")
else:
    print("doesn't work")
    
will work
    a = 0.6 + 0.2
    b = 0.8

    if(a==b):
        print("works")
    else:
        print("doesn't work")
    
    
to fix it, you can use approximate comparison

example

a = 0.1 + 0.2
b = 0.3

epsilon = 1e - 10 #small tolerance value

if(abs(a-b) < epsilon):
    print("a is approximately equal to b")
else:
    print("a is not equal to b")


"""
