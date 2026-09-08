"""
email: adel.alam@torontomu.ca
Student ID: 501293305

Create a program that ties in the user's bank account and their grocery list.
The user needs to provide items they want to add to a list and the price that 
their items cost. The user also needs to deposit money into their account
to compare with the sum of the total grocery costs to see if they can afford it.
If they can't, they get various options to choose from. If they can't afford something
they can remove items or they can get advice for compound interest. If they don't 
do either then they will go straight to the main menu. If they can afford it then they can add 
more items or just go straight to main menu. Once at the main menu, they get options to add, change
or remove items. When they do any one of these 3, the output text file will be updated alongside the 
in-program list. There will also be options to view the list, check for bank balance again,
or go straight into the compound interest calculations as well, all in the main menu. Once
the user is done, they have the option to quit the program as well.

"""

"""*******************************************************
PLEASE ENTER THE EXACT INPUTS AS THE COMMANDS REQUEST. THIS ISN'T GETTING MARKED FOR ERROR HANDLING
SO I DIDN'T ACCOUNT FOR IT. IF THE PRORGAM BREAKS BECAUSE OF IMPROPER NOTATION, NOT MY FAULT
***********************************************************"""

"""All of these variables are used to modify list of items, price of items, and total costs depending
on the needs of each function. These 3 are the back bone of the program. Without them
this program won't work."""
groceryList = []
groceryCost = []
sumCost = 0.0


"""This function is used to consistently update the grocery list as the user continues
to add, remove, change, clear or set the grocery list. This list is update in the text
file named "groceryList.txt" and it will only write to the file, doesn't read from it
anywhere. The test value isn't very useful. its only for the first instance when the 
list is being created when the program is initialized, so after the first iteration
its pointless"""


def writeToFile(test=0):
    global groceryList
    global groceryCost
    with open("groceryList.txt", "w") as myFile:

        for i in range(len(groceryList)):
            myFile.write(f"{(i+1)}. {groceryList[i]}, ${groceryCost[i]}\n")
    if (test == 1):
        getBankBalance()
    elif (test == 0):
        mainMenu()


"""This function is used to remove items from a list. It asks the user for how many values
for the range of the loop and the index values in the loop. It also removes the cost of the item from sumCost variable 
as well to make sure total cost is updated. After removing the values it writes to file"""


def removeItem():
    global groceryList
    global groceryCost
    global sumCost
    userIterator = int(input("How many values do you want to remove? "))

    for i in range(userIterator):
        userVal = int(input("Please enter the index number to remove: "))
        del groceryList[userVal-1]
        sumCost -= float(groceryCost[userVal-1])
        del groceryCost[userVal-1]

    writeToFile()


"""This function is used to add items to a list. It asks the user for how many values
for the range of the loop and appends values from end of list. It also adds the cost of the item to sumCost variable 
as well to make sure total cost is updated. After adding the values it writes to file"""


def addItems():
    global groceryList
    global groceryCost
    global sumCost
    userIterator = int(input("How many values do you want to add? "))

    for i in range(userIterator):

        userVal = input("Please enter an item to add to the list: ")
        groceryList.append(userVal)
        userVal = input(
            "Please enter the price of the item (without dollar sign): ")
        groceryCost.append(userVal)
        sumCost += float(userVal)

    writeToFile()


"""This function is used to change items in a list. It asks the user for how many values
for the range of the loop and the index values in the loop to change. It also changes the cost of the item from sumCost variable 
as well to make sure total cost is updated. It subtracts the old price and adds the new price. After changing the values it writes to file"""


def changeItem():
    global groceryList
    global groceryCost
    global sumCost
    userIterator = int(input("How many values do you want to change? "))

    for i in range(userIterator):
        userIndex = int(
            input("Please enter an item number to change in the list: "))
        userVal = input("What is the new item? ")
        newPrice = float(
            input("What is the new price (without dollar sign)? "))
        groceryList[userIndex-1] = userVal
        sumCost -= float(groceryCost[userIndex-1])
        groceryCost[userIndex-1] = newPrice
        sumCost += float(newPrice)
    writeToFile()


"""This function does some basic math calculation for finding compounded values. 
This function also has a user defined variable that will get a dollar amount to use to 
calculate the compounded interest based on which option the user chooses. It also has 
the option of returning the user to the main menu if they change their mind. Returns to 
main menu after interest calculation is done"""


def moneyOperation(moneyAmnt=0):  # user defined function
    # add an option to give the user an option to get a loan and give them estimated
    # costs with the loan
    print("\nWelcome to the Finance Portal")
    print("""These are your options Note that these are advices and will not directly impact your bank account. Its to give you options to think
about (not guranteed to cover all grocery costs):
1 - Higher Interest, longer time (20% for 2 years with 3 installments per year)
2 - Less Expensive Amortized Loan (35% for 1 year with 1 installment)
3 - Go to main menu\n""")

    user = input(
        "\nWhat choice do you wish to make? Please type in the index number: ")
    if (user == "1"):
        compounded = moneyAmnt * (1+0.2/3)**(3*2)
        print(
            f"\n\nSince you chose option 1, you are expected to earn ${round(compounded,2)} over 2 years")

    elif (user == "2"):
        compounded = moneyAmnt * (1+0.35/1)**1
        print(
            f"\n\nSince you chose option 2, you are expected to earn ${round(compounded,2)} over 1 year")

    elif (user == "3"):
        print("\n\nReturning to main menu")
        mainMenu()
    print("\n\nReturning to main menu")
    mainMenu()


"""This is a big function. It has many parts to it which I will delve into deeper.
Main information about this function is that it makes comparisons with the amount of money
the user inputs within the function to give them the best next option possible"""


def getBankBalance():
    # user defined variable
    bankAmount = float(
        input("Please enter the amount of money you have in your bank: "))

    difference = 0

    """Comparison 1: This comparison is responsible checking to see if the user has less money than what 
    their grocery list is worth. The difference calculation is used to check the deficit amount"""
    if (bankAmount < sumCost):

        difference = sumCost - bankAmount

        user = input((f"""Do you want to think about investing some money? You currently have a deficit 
of ${difference}. Type y or n: """))

        """Comparison 1.1: if user chooses y then they get sent to the moneyOperation function where they 
        have the option in seeing some interest plans to invest money (albeit not the best short term option.)"""
        if (user.lower() == "y"):
            moneyOperation(bankAmount)

            """Comparison 1.2: User types n meaning they dont want to invest. They now have the option to remove items
            through the remove items function or to do nothing again and get sent to the main menu. """
        elif (user.lower() == "n"):
            user = input(("""Do you wish to remove an item from the grocery 
list? Type y or n: """))

            """Comparison 1.2A: Sends user to remove item function where lists are updated, and updates the text file as well."""
            if (user.lower() == "y"):
                removeItem()

                """Comparison 1.2B: User chooses to do nothing so they get sent to the main menu where they can do other stuff. If they want to update
                their money amount they can, by re-entering the checkbalance function."""
            elif (user.lower() == "n"):
                print("Unfortunately you can't buy every item in the list you provided")
                print("Returning to main menu")
                mainMenu()

        """Comparison 2: This comparison checks to see if the user has more money than what their grocery list is worth.
        The surplus calculation is used to check how much money is left over after the price of groceries is subtracted.
        User is then given options that they can choose"""
    elif (bankAmount > sumCost):
        surplus = bankAmount - sumCost
        user = input((f"""You currently have a surplus of ${surplus}. Do you want to add
more items to your list? Type y or n: """))

        """Comparison 2.1: This comparison sends user to add items where all the global variables are updated 
        and the list is also updated"""
        if (user.lower() == "y"):
            addItems()

            """Comparison 2.2: This comparison sends user to main menu since they chose to do nothing"""
        elif (user.lower() == "n"):
            print("Going to main menu\n\n")
            mainMenu()

        """This condition implies that the user has enough in their bank account to afford their items on the dot.
        Lets the user know that, and then sends them to the main menu"""
    else:
        print("You have exact amount of money required!")
        print("Returning to main menu")
        mainMenu()


"""This is the first function that runs. It intializes the user's initial list. This also sums the total cost
for comparison in other functions later when the user chooses to do other stuff through the main menu."""


def setList():
    global groceryList
    global groceryCost
    global sumCost
    print("\n\nWelcome to Grocery and Banks. I will ask for your grocery list and bank amount first")
    print("For dollar amount, you can include cents without dollar sign")

    """This is the while loop requirement. User inputs the item first then inputs the cost as these 2 values are saved
    in 2 different lists. I tried to do it one line using map function but I don't think I was doing it right."""
    while (True):
        user = input("Please enter an item: ")
        groceryList.append(user)
        user = input("Please enter the cost: ")
        sumCost += int(user)
        groceryCost.append(user)

        user = input(
            "Is ur list done? Type \"end\" if you're done, type anything else if you're not: ")

        """Loop only ends when the user types end. If the user doesn't type end, its basically an infinite loop.
        If they type something the list ends and goes on to write the grocery list to the write file to set the textfile or create
        it, if it was deleted"""
        if (user.lower() == "end"):
            writeToFile(1)
            break


"""This is another recurring function. It's only purpose is to print the list. The function's boolean input is only there to separate 
the user's intentions. If the user only wants to see the list then it goes to the loop by flipping boolVal to True thus making it an
infinite loop until user types y to leave and return to main menu. If the user does not want to see the list, then boolean is set to false
so that the list can be displayed on top of the other functions the user wants to execute to make it more user friendly, and so the user doesn't 
have to keep the grocery list open all the time and reopen it everytime a change is done."""


def printList(boolVal=False):
    print("Here is your current list:\n")

    for i in range(len(groceryList)):
        print(f"{(i+1)}. {groceryList[i]}, ${groceryCost[i]}\n")
    while (boolVal):
        user = input("Do you want to return to main menu? Type y/n: ")

        if (user == "y"):
            mainMenu()
            break


"""Main menu where user can do anything they want within the 7 options.
It's pretty self explanatory as to what each option will do so there's not much to go
in depth about."""


def mainMenu():
    print("\n\nWelcome the Main Menu of this program")
    print("""Below are some options you can select to navigate to where you want to go
0 - Display List
1 - Add Items to list 
2 - Remove Items from list
3 - Change Items in your list
4 - Check Bank Balance
5 - Check Interest Options
6 - Clear List
7 - Quit """)

    user = input("\nChoose an index number: ")
    if (user == "0"):
        printList(True)

    elif (user == "1"):
        printList()
        addItems()

    elif (user == "2"):
        printList()
        removeItem()

    elif (user == "3"):
        printList()
        changeItem()

    elif (user == "4"):
        getBankBalance()

    elif (user == "5"):
        user = float(
            input("Please enter a bank amount to compare interest rates with: "))
        moneyOperation(user)

    elif (user == "6"):
        groceryList.clear()
        groceryCost.clear()
        print("\n\nList is emptied")
        writeToFile()
    elif (user == "7"):
        print("Thank you for choosing this program")

    else:
        print("Choose proper option")
        mainMenu()


"""This initializes the program by going to set list function and running the entire
program"""
setList()
