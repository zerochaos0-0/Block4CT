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
        print("Hello, there! Let's work with lists!")
        print("Choose one of the following opitons. Type a number ONLY!")
        choice = input("""1. Add to list,
2. Return the value at an index position,
3. Generate a random number from the list
4. End the program   """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "4":
            break
        elif choice == "3":
            randomSearch()
    #we need to add an exit program as well as error catching

        
def addToList():
    print("Okay, you want to add to your list!")
    newItem = input("What interger would you like to add?  ")
    myList.append(int(newItem))
    print(myList)

def indexValues():
    indexPos = input("Which index position would you like to know?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("Here's a random value from your list!")
    print(myList[random.randint(0, len(myList)-1)])

if __name__ == "__main__":
    mainProgram()
