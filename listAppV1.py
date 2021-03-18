"""

Program Goals:
1. Get the input from the user
2. Convert that input to an int
3. Add that input to a list
4. Pull values from specific index positions
"""

#create functions that will perform the above actions
import random
myList = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose one of the following opitons. Type a number ONLY!")
            choice = input("""
1. Add individual integers to list,
2. Add multiple integers to your list,
3. Return the value at an index position,
4. Generate a random number from the list, 
5. Print your current list,
6. Linear Search
7. End the program   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                print(myList)
            elif choice == "6":
                linearSearch()
            else:
                break
        except:
            print("An error occurred.")
        
def addToList():
    print("Okay, you want to add to your list!")
    newItem = input("What interger would you like to add?  ")
    myList.append(int(newItem))
    print(myList)

def addABunch():
    print("We're gonna add a bunch of numbers!")
    numToAdd = input("How many intergers do you want to add?  ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete!")

def indexValues():
    indexPos = input("Which index position would you like to know?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search through the list in the WORST WAY POSSIBLE!")
    searchItem = input("What are you looking for? Number-wise?  ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index {}".format(x))
        

if __name__ == "__main__":
    mainProgram()
