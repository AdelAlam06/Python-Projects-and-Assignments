N = int(input("Please enter a number: "))

if(N > 100):
    print("Too much work, no thanks")

elif(N < 1):
        print("N must be greater than 1")
else:
    for i in range(1,N+1):

        if(i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)