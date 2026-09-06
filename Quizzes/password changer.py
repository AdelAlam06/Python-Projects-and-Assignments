
userInput = input("Please enter a password: ")
userInput2 = input("Please reenter the password: ")

if(userInput == userInput2):
    
    for char in userInput:
        checkUpper = char.isupper()
        if(checkUpper == True):
            break
        
    for char in userInput:
        checkLower = char.islower()
        if(checkLower == True):
            break
    
    if(len(userInput) >= 8 and userInput.isalnum() == True and userInput.islower() == False
       and userInput.isupper() == False):
        
        print("Password changed successfully")
    else:
        print("Password not complex enough")
else:
    print("Passwords must match")
