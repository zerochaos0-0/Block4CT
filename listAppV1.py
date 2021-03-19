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


def mainProgram():
    while True:
        try:
            print("So you wanna make a number list? Alright bet let's get to it!")
            time.sleep(1.5)
            print("Kindly choose one of the following options. Make sure you only type a number!")
            time.sleep(1.5)
            choice = input("""
1. Add individual integers to your list,
2. Add multiple integers to your list,
3. Return the value at an index position,
4. Generate a random number from the list, 
5. Search your list for a specific number,
6. Print your current list,
7. End the program   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "6":
                print(myList)
            elif choice == "5":
                linearSearch()
            else:
                break
        except:
            print("Woah there bud, that's not a number.")
        
def addToList():
    print("Okay, you want to add to your list!")
    time.sleep(1.5)
    newItem = input("What interger would you like to add?  ")
    myList.append(int(newItem))
    readList = input("Would you like to see your new list? y/n?  ")
    if readList == "y":
        print("No problem, here ya go!")
        time.sleep(1.5)
        print(myList)
    elif readList == "n":
        print("That's all good dude. ")


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
    if readList == "y":
        print("No problem, here ya go!")
        time.sleep(1.5)
        print(myList)
    elif readList == "n":
        print("That's all good dude. ")

def indexValues():
    indexPos = input("Which index position would you like to know?  ")
    time.sleep(1.5)
    print("Here you are...")
    time.sleep(1)
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list!")
    time.sleep(1.5)
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list in the WORST WAY POSSIBLE!")
    time.sleep(1.5)
    searchItem = input("What are you looking for? Number-wise?  ")
    indexCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            indexCount = indexCount + 1
            print("Your item is at index {}".format(x))
    print("Your number appeared {} times in the list".format(indexCount))


if __name__ == "__main__":
    mainProgram()
