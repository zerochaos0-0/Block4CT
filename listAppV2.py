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

"""
This is the main function of the program that greets the user,
providing them with the options of which menu they would like to choose from.
They may either be sent to the search menu, the edit menu, print their list,
or leave the program, which is done using if/elif/else statements,
which send the user to the accompanied functions. This is all done in a while loop,
so the user always returns to the main menu when they are done with each action.
"""

def mainMenu():
    print("Hello user! Welcome to the Main Menu of Ricardo's Online List Empire!")
    time.sleep(1.5)
    print("You're here which obviously means you would like to make a list.")
    time.sleep(1.5)
    while True:
        print("To get started with your list, choose from the following options.")
        time.sleep(1)
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
        elif choice == "4":
            print("We're very sad to see you go, and hope you have a great day.")
            break
     
"""
This function works by first being called in the mainMenu() function when the user
chooses to go to the search menu. Under this function, the user is provided with a
variety of options to search their list, though first the list must of course have
items stored in it. When the user enters the searchMenu() function, they are
confronted with five search options, a classic linear search, a random search,
index search, as well as iterative and recursive binary searches, all of which
work in their own respective functions.
"""
       
def searchMenu():
    print("Welcome to the Search Menu! Here you will find all options to search your list.")
    time.sleep(1)
    print("You know the rules, select which option you want, but ONLY type the number!")
    time.sleep(1)
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
        print("Coming right up!")
        time.sleep(1)
        print("Searching...")
        time.sleep(2)
        print("Search Complete!")
        time.sleep(1)
        recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
        time.sleep(.5)
    elif searchMenus == "5":
        binSearch = input("What number are you looking for?  ")
        result = iterativeBinarySearch(unique_list, int(binSearch))
        print("Coming right up!")
        time.sleep(1)
        print("Searching...")
        time.sleep(2)
        print("Search Complete!")
        time.sleep(1)
        if result != -1:
            print("Your number is at index position {}".format(result))
            time.sleep(.5)
        else:
            print("Your number is not found in that list my guy!")
            time.sleep(.5)
    else:
        mainMenu()
        time.sleep(1)

"""
Like the searchMenu() function, the editMenu() function is called in the
mainMenu() function when the program asks the user where they would like to go.
This function provides the user with a limited choice of options of ways to
edit their list, they can either add to their list or clear their list,
both options work in their own respective functions.  
"""

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

"""
This function works by first asking the user if they would like to add individual
numbers to their list or if they would like to add multiple numbers.
Based on the user’s input they are either moved to the addABunch() function,
or they stay in the addToList() function. If the user stays in the addToList() function,
they are then asked how mant individual numbers they would like to add.
This information is transferred from string form to integer form and
the user is sent to the multipleIndividuals() function.
"""

def addToList():
    print("Okay, you want to add to your list!")
    time.sleep(1.5)
    whichFunction = input("So first, would you like to add individual numbers or a bunch? Say 'individual' or 'bunch'   ")
    if whichFunction == "individual":
        y = input("Okay, How many individual numbers do you want to add to your list?  ")
        y = int(y)
        multipleIndividuals(y)
        time.sleep(.5)
    elif whichFunction == "bunch":
        print("A bunch it is!")
        addABunch()
        time.sleep(.5)

"""
This function works by first being called in the addToList() function,
where the user makes the choice if they would like to add numbers individually
or multiple at a time, if the user chooses to add multiple numbers, they’re sent here! 
The user is asked to input how many numbers they want to add and
how high they want these numbers to go. This information is then changed from
strings to integers. These are then put in a for loop which uses the integer
version of the input of how high the user want their numbers as the range.
Using the .append method, the program takes the integer version of the user’s input
of how many numbers they want to add, and adds that many random numbers
using the .randint method. Finally, after giving the user the choice to print their list,
the program asks the user if they would like their list sorted before it is printed to them.
If the user wants their list printed as is, without sorting, the program does so,
however if they would like their list to be sorted, they are then moved
to the sortList() function. 
"""

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

"""
This function works by first being called in the addABunch() and multipleIndividuals()
functions, when the user chooses to have their list sorted.
Using a for loop and a second list called unique_list, the program checks each number
in myList to see if it is already in unique_list, if it is,
that number is disregarded and the program moves onto the next number. However,
if the number is not in unique_list, the program then adds that number to
unique_list using the .append method. Finally, after the program has ran
through every number in myList, it prints unique_list to the user.
"""

def sortList(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    time.sleep(1)
    print(unique_list)
    time.sleep(1)

"""
This function works by first being called in the searchMenu() function,
when the user chooses to search a specific index position of their list.
The program takes the integer verison of the user’s input of what
position in their list they would like to search and uses to then
print that position from myList.
"""

def indexValues():
    print("What index position would you like to check?")
    indexPos = input("")
    time.sleep(1)
    print("Checking...")
    time.sleep(1)
    print("Here you go! Your number is {}".format(myList[int(indexPos)]))
    time.sleep(1)

"""
This function works by first being called in the searchMenu() function,
when the user chooses to generate a random number from their list.
The program uses the len() function to find out how many objects are
in myList, and uses the .randint method to randomly select
one of those objects and returns the chosen number to the user.
"""

def randomSearch():
    print("You got it!")
    time.sleep(1)
    print("Randomizing list...")
    time.sleep(1)
    print("Generating number...")
    time.sleep(1)
    print("Your number is {}".format(myList[random.randint(0, len(myList)-1)]))
    time.sleep(1)      

"""
This functions works by first being called in the searchMenu() function,
when the user chooses to search their list for a specific number.
The user is asked what number they would like to search their list for,
then using a for loop the program takes the integer version of the number
the user inputted and finds every place in myList where that number occurs
and returns it to the user. Finally, it tallies up how many times that
number appears in the list and returns that information to the user.
It does this by making indexCount equal to zero, and each time that number
is found in the list, the program adds one to indexCount.
"""

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

"""
This function works by first being called in the searchList() function,
when the user chooses to recursively search their list. Using the arguments
unique_list, low, high, and x, the function recursively widdles the list down
using the highest, lowest, and middle points in the list until the mid point
is equal to the number that the user is looking for, as long as that number appears
in unique_list.
"""

def recursiveBinarySearch(unique_list, low, high, x):
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

"""
This function works by first being called in the searchList() function,
when the user chooses to iteratively search their list. Using the arguments
unique_list, low, high, and x, the function widdles the list down
using the highest, lowest, and middle points in the list until the mid point
is equal to the number that the user is looking for, as long as that number appears
in unique_list.
"""

def iterativeBinarySearch(unique_list, x):
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

"""
This function works by first being called in the mainMenu() function,
when the user chooses to print their list(s). The program uses the len()
function to check if there are any numbers in unique_list, if not,
it automatically prints myList. However if unique_list isn’t empty,
then the program asks the user if they would like their sorted list printed
or their unsorted list printed. If they want their sorted list printed,
then the program prints unique_list, however if they want their sorted
list printed the program prints myList.
"""

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

"""

This functions works by first being called in the editMenu() function,
when the user chooses to clear their list. The user is asked again
if they would like to clear their list, as a precaution, then if
the user replies yes, myList is then cleared. 


"""

def clearList():
    clearList = input("So you want to clear your list, is that correct? y/n?   ")
    if clearList == "y":
        print("You got it!")
        myList.clear()
        print("Presto chango, your list is cleared!")
    else:
        print("No problem, ace!")

"""

This function works by first being called in the addToList() function,
where the user is asked how many numbers they would like to add.
This number is then transferred to from str to int and the program
uses a for loop to append these numbers to myList.


"""

def multipleIndividuals(y):
    for x in range(y):
        newNum = input("What number do you want to add?  ")
        myList.append(int(newNum))
    print("Your list is now complete!  ")
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
    

if __name__ == "__main__":
    mainMenu()
