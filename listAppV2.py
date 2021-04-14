"""

Program Goals:
1. Get the input from the user
2. Convert that input to an int
3. Add that input to a list
4. Pull values from specific index positions
"""

#create functions that will perform the above actions
import random
import time
myList = []
unique_list = []


def mainMenu():
    print("Hello user! Welcome to the Main Menu of Ricardo's Online List Empire!")
    time.sleep(2)
    print("You're here which obviously means you would like to make a list.")
    time.sleep(2)
    while True:
        print("To get started with your list, choose from the following options.")
        time.sleep(2)
        print("Remember, you can only write a number!")
        time.sleep(1)
        choice = input("""
1. Transport to the Edit List Menu,
2. Transport to the Search List Menu,
3. Print Your List,
4. Leave Ricardo's Online List Empire    """)
        if choice == "1":
            editMenu()
            time.sleep(1)
        elif choice == "2":
            searchMenu()
            time.sleep(1)
        elif choice == "3":
            printLists()
            time.sleep(1)
        else:
            print("We're very sad to see you go, and hope you have a great day.")
            break
            
def searchMenu():
    print("Welcome to the Search Menu! Here you will find all options to search your list.")
    time.sleep(1)
    print("You know the rules, select which option you want, but ONLY type the number!")
    searchMenus = input("""
1. Search your list for any number you desire,
2. Generate a random number from your list, 
3. Ask the all-knowing program what number is at a certain position,
4. Recursively search your sorted list,
5. Iteratively search your sorted list,
6. Return to Ricardo's Online List Empire Main Menu    """)
    if searchMenus == "1":
        linearSearch()
        time.sleep(1)
    elif searchMenus == "2":
        randomSearch()
        time.sleep(1)
    elif searchMenus == "3":
        indexValues()
        time.sleep(1)
    elif searchMenus == "4":
        binSearch = input("What number are you looking for?  ")
        recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
        time.sleep(.5)
    elif searchMenus == "5":
        binSearch = input("What number are you looking for?  ")
        result = iterativeBinarySearch(unique_list, int(binSearch))
        if result != -1:
            print("Your number is at index position {}".format(result))
            time.sleep(.5)
        else:
            print("Your number is not found in that list my guy!")
            time.sleep(.5)
    else:
        mainMenu()
        time.sleep(1)
def editMenu():
    print("Welcome to the Edit Menu! Here you will find all options to edit your list.")
    time.sleep(1)
    print("You know the rules, select which option you want, but ONLY type the number!")
    editMenus = input("""
1. Add to your list,
2. Clear your list of all numbers,
3. Return to Ricardo's Online List Empire Main Menu    """)

    if editMenus == "1":
        addToList()
        time.sleep(1)
    elif editMenus == "2":
        clearList()
        time.sleep(1)
    else:
        mainMenu()
        time.sleep(1)

def addToList():
    print("Okay, you want to add to your list!")
    time.sleep(1.5)
    whichFunction = input("So first, would you like to add individual numbers or a bunch? Say 'individual' or 'bunch'   ")
    if whichFunction == "individual":
        print("Got it! Let's add a number!")
        newItem = input("What number would you like to add?  ")
        myList.append(int(newItem))
        print("Your list is now complete!")
        seeList = input("Would you like to see your list? y/n?  ")
        if seeList == "y":
            print("Got it!")
            sortedList = input("Would you like the list sorted, or unsorted?   ")
            if sortedList == "sorted":
                print("Sorted list, coming right up!")
                sortList(myList)
            elif sortedList == "unsorted":
                print("Unsorted it is!")
                time.sleep(1)
                print(myList)
        elif seeList == "n":
            print("No problem, partner!")
            time.sleep(1)
    elif whichFunction == "bunch":
        print("A bunch it is!")
        addABunch()
        time.sleep(.5)

def addABunch():
    print("Let's get to adding some numbers!")
    time.sleep(1)
    numToAdd = input("How many numbers would you want to add to your list?  ")
    time.sleep(1)
    numRange = input("And how high would you like these numbers to go?   ")
    time.sleep(1)
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete!")
    seeList = input("Would you like to see your list? y/n?  ")
    if seeList == "y":
        print("Got it!")
        sortedList = input("Would you like the list sorted, or unsorted?   ")
        if sortedList == "sorted":
            print("Sorted list, coming right up!")
            sortList(myList)
        elif sortedList == "unsorted":
            print("Unsorted it is!")
            time.sleep(1)
            print(myList)
    elif seeList == "n":
        print("No problem, partner!")
        time.sleep(1)
            
def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    time.sleep(1)
    print(unique_list)
    time.sleep(1)


def indexValues():
    print("What index position would you like to check?")
    indexPos = input("")
    time.sleep(1)
    print("Here you go...")
    time.sleep(.5)
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list!")
    time.sleep(1.5)
    print(myList[random.randint(0, len(myList)-1)])
    time.sleep(2)


def linearSearch():
    print("Okay, let's search your list!")
    time.sleep(1.5)
    searchItem = input("What number would you like to find in your list?  ")
    print("Coming right up!")
    time.sleep(1)
    print("Searching...")
    time.sleep(2)
    print("Search Complete!")
    time.sleep(1)
    indexCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item is at index {}".format(x))
    print("Your number appeared {} times in the list".format(indexCount))
    time.sleep(2)

def recursiveBinarySearch(unique_list, low, high, x):
    print("Coming right up!")
    time.sleep(1)
    print("Searching...")
    time.sleep(2)
    print("Search Complete!")
    time.sleep(1)
    if high >= low:
        mid = (high + low) // 2
        
        if unique_list[mid] == x:
            print("Your number is at position {}".format(mid))
            return mid

        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    print("Coming right up!")
    time.sleep(1)
    print("Searching...")
    time.sleep(2)
    print("Search Complete!")
    time.sleep(1)
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


def printLists():
    if len(unique_list) == 0:
        print(myList)
        time.sleep(1.5)
    else:
        whichOne = input("Which list? Sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
            time.sleep(1.5)
        elif whichOne.lower() == "unsorted":
            print(myList)
            time.sleep(1.5)

def clearList():
    clearList = input("So you want to clear your list, is that correct? y/n?   ")
    if clearList == "y":
        print("You got it!")
        myList.clear()
        print("Presto chango, your list is cleared!")
    else:
        print("No problem, ace!")



if __name__ == "__main__":
    mainMenu()
