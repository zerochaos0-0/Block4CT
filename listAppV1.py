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


def mainProgram():
    while True:
        try:
            print("So you wanna make a number list? Alright bet let's get to it!")
            time.sleep(1)
            print("Kindly choose one of the following options. Make sure you only type a number!")
            time.sleep(1.5)
            choice = input("""
1. Add individual numbers to your list,
2. Add multiple numbers to your list,
3. Return the value at an index position,
4. Generate a random number from the list, 
5. Search your list for a specific number,
6. Sort your list,
7. Print your list,
8. End the program   """)
            if choice == "1":
                addToList()
                time.sleep(.5)
            elif choice == "2":
                addABunch()
                time.sleep(.5)
            elif choice == "3":
                indexValues()
                time.sleep(.5)
            elif choice == "4":
                randomSearch()
                time.sleep(.5)
            elif choice == "5":
                linearSearch()
                time.sleep(.5)
            elif choice == "6":
                sortList(myList)
                time.sleep(.5)
            elif choice == "7":
                printLists()
                time.sleep(.5)
            else:
                break
        except:
            print("Woah there bud, that's not a number.")
            time.sleep(2)

        
def addToList():
    print("Okay, you want to add to your list!")
    time.sleep(1.5)
    newItem = input("What interger would you like to add?  ")
    myList.append(int(newItem))
    readList = input("Would you like to see your new list? y/n?  ")
    if readList.lower() == "y":
        print("No problem, here ya go!")
        time.sleep(1.5)
        print(myList)
        time.sleep(3)
    elif readList.lower() == "n":
        print("That's all good dude. ")
        time.sleep(1.5)


def addABunch():
    print("Cool cool, let's add some numbers!")
    time.sleep(1.5)
    numToAdd = input("How many intergers do you want to add?  ")
    time.sleep(1.5)
    numRange = input("And how high would you like these numbers to go?   ")
    time.sleep(1.5)
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete!")
    readList = input("Would you like to see your new list? y/n?  ")
    if readList.lower() == "y":
        print("No problem, here ya go!")
        time.sleep(1.5)
        print(myList)
        time.sleep(3)
    elif readList.lower() == "n":
        print("That's all good dude. ")
        time.sleep(1.5)

def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = ("Would you like to see your new list? y/n?  ")
    if showMe.lower() == "y":
        print("No problem, here ya go!")
        time.sleep(1.5)
        print(unique_list)
        time.sleep(3)
    elif showMe.lower() == "n":
        ("That's all good dude. ")
        time.sleep(1.5)


def indexValues():
    indexPos = input("Which index position would you like to know?  ")
    time.sleep(1.5)
    print("Here you are...")
    time.sleep(1)
    print(myList[int(indexPos)])
    time.sleep(2)

def randomSearch():
    print("Here's a random value from your list!")
    time.sleep(1.5)
    print(myList[random.randint(0, len(myList)-1)])
    time.sleep(2)


def linearSearch():
    print("Okay, let's search your list!")
    time.sleep(1.5)
    searchItem = input("What are number would you like to find?  ")
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
    if high >= low:
        mid = (high + low) // 2
        
        if unique_list[mid] == x:
            print("Oh, what luck! Your number is at position {}".format(mid))
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def printLists():
    if len(uniques_list) == 0:
        print(myList)
        time.sleep(1.5)
    else:
        whichOne = input("Which list? Sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
            time.sleep(1.5)


if __name__ == "__main__":
    mainProgram()
