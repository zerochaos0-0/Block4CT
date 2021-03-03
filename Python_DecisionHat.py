import random
import time

#OVERVIEW OF PROGRAM
#The purpose of this program is to be able to use an input function to allow the user to put a list of things into a hat and pull one of those things out of the hat
#(For example you put 6 pieces of paper into the hat, each labeled with a different thing, the hat is intended to give you one of the things out of the list, perfect for any decision)


#FEATURES TO ADD:
#Put a stall between when the user puts the things into the hat and when the hat returns a piece of paper


myDraws = []

t = 1.5

print("Hiya! Are you indecisive? Well then step on up to the Hat of Decisions!!")

def hatEngine():
    userList = []
    while True:
        newItem = input("What would you like to add?  ")
        userList.append(newItem)
        keepGoing = input("Keep going y/n?  ")
        if keepGoing == "n":
            break
        else:
            pass
    
    drawAPaper = input("Would you like the hat to make a decision for you? y/n  ")

    if drawAPaper == "n":
        print("Wow, thanks for wasting my time. Get outta here!!")

    elif drawAPaper == "y":
        print("Okay, one decision coming right up!")
        time.sleep(1.5)
        print("The hat has decided...")
        time.sleep(1.5)
        print(userList[random.randint(0,len(userList)-1)])
        time.sleep(1.5)
        print("Have a very good day!")


if __name__ == "__main__":
    hatEngine()
