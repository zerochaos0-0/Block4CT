Software Instructions:
	1. Obviously before doing anything you have to open the program and run the application
	2. You're greeted by Ricardo's Online List Empire, and provided with a list of options. In order for the application to work you first have to make sure to add
	items to your list, as you can't do anything with an empty list. Also remember, you can ONLY ENTER A NUMBER.
	3. Once you have added to your list, the next step is to search it, which means you have to go to the edit menu
	4. In the edit menu you can choose between many options to search your list, however before you can do the recursive or iterative search you have to make sure
	your list has been sorted. If it hasn't they will automatically return that the list is empty, as the sorted list is a seperate list, and needs to be in order 
	or the search will not work properly
	5. If you want to make a new list, go into the edit list menu and select the clear list option where the application double checks that you would like to clear 
	your list, then does so once you have verified it's what you want
	6. From there it's really up to you as to what to do, just have fun and make sure to always ONLY ENTER A NUMBER

Note: If you do not follow the instructions, it's likely the code will return you with a long list of errors in aggressive red text 

How the two Binary Search algorithms work:

The binary search works by specifically using unique_list because it is the version of myList that has been sorted and 
has gotten rid of repeat numbers, meaning it's a list in the form of 0,1,2,3,etc. instead of 6,3,4,6,etc. like myList.

The recursive search works by first calling unique_list, x (x being the value that the user asked the application for), low, and high. It does this so that there is a 
way to recursively widdle the list down to return the user the number they want as well as it's position. The application then says that if high is greater than or equal 
to low, then mid (mid being what will eventually be returned to the user as their number) is equal to high plus low divided by two. The application then says that if mid
is equal to x, return mid to the user. However if mid is greater than x, it calls the function within itself, and sends it back to the beginning, however this time high is equal
to mid minus one, effectively getting rid of half of the list. The same thing happens if mid is less than x, however in that case low is equal to mid plus one. It continues to 
do this until mid is equal to x, when it returns it to the user, along with the index position. The only danger with recursive searches is getting caught in a loop, when the 
application is constantly calling itself, causing the computer to crash.

The iterative search is able to acheive the same result as the recursive search by first calling unique_list and x (x being the value that the user asked the 
application for), then recognizing low and mid as zero, because we need to make sure that both of those variables exist and can be used by the application to 
find the number the user wants. It then recognizes high as the total number of items in unique_list, minus one to account for index position zero. After we set 
up the initial variables, the next thing that has to happen is we have to make it true that while low is less than or equal to high, 
mid equals high plus low divided by two. The reason this needs to happen is because eventually the mid point is going to be widdled down
to be equal to the number the user asked the application to find. Next using an if/elif/else statement, the application says that if mid is greater than x, then 
low is now equal to mid plus 1. This means that now the low point is equal to one greater than the mid point so when the application runs through that bit of code 
again, it's only working with half of the list and is still keeping track of the index point. However, if mid is less than x, the application then does the same thing,
however makes the high value equal to the mid value minus 1. The application continues to do this until the mid point is equal to x, when that is true, 
the application returns the mid point to the user as well as what index position it was in. 

Changes I made:

	- user-friendliness 
		- why it helped the application: Making the language of the application less complex makes it much easier for the user to work through the different options
		of making a list . Using language like "recursive binary search", "iterative binary search", "integer", "string", etc. may be all fine and dandy for a programmer
		to understand, but to most people it's like attempting to understand the Declaration of Independence. Using the time.sleep() method allows the text
		that the user has to read to come at them much much slower, so they can process it and aren't reading a whole paragraph at once. Finally, making the
		interface more entertaining makes it easier for the user to use, as sometimes it can get tedious so having more entertaining text can make it more fun.
	- clear list 
		- why it helped the application: Adding the clear list function allows the user to use the application over and over again, with multiple random lists
		without having to close it and rerun.
	- adding multiple individual numbers 
		- why it helped the application: This function gives the user the ability to add multiple numbers OF THEIR CHOICE, instead of randomized numbers like the 
		addABunch() function does. The beauty of this function is that you can also make the choice to only add one number, so you don't HAVE to add multiple if
		you don't want.
	- deciding if you want your list sorted when it is printed to you (instead of a sort function) 
		- why it helped the application: This basically just combines two functions into one, making it so that the user doesn't have to move back and forth between
		functions, and can just do it all at once. When they add items to their list, the application automatically asks if they want their list printed, and if so
		it asks whether they want a sorted list or an unsorted list, if they want it sorted the application then switches over to the sort list function and sorts myList
		into unique_list before printing it to the user. 
	- mainMenu, searchMenu, and editMenu
		- why it helped the application: This minimizes the amount of text that the user has to process at once, and actually makes the decision making process
		easier because they can tell based on which menu the choice is in what it does, instead of one large list.
	- combining all of the add to list functions 
 		- why it helped the application: Moving all of the add to list functions into one makes it much easier for the user to add to their list, as they don't
		have to move between selections, the application does it for them! 

	how it could be improved: if the user tries to do one of the binary searches before sorting their list the program will always return that the item is not 
			there because the list it is searching is empty, the only way to sort your list is after adding to it you're asked if you want your 
			list sorted, using buttons instead of having to type the numbers to select
Examples of new lines of code I wrote:

Combined Add to List Functions: 

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

Clear List Function: 

def clearList():
    clearList = input("So you want to clear your list, is that correct? y/n?   ")
    if clearList == "y":
        print("You got it!")
        myList.clear()
        unique_list.clear()
        print("Presto chango, your list is cleared!")
    else:
        print("No problem, ace!")

Adding multiple individual numbers & printing a sorted list:

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
