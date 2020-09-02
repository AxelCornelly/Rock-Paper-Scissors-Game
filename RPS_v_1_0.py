# Rock Paper Scissors Game
# Last Modified: 09/01/2020
# V 1.0
# Author: Axel Cornelly
"""
Summary: Rock, Paper, Scissors program
in which the user can play against the computer!
The user will be prompted to pick rock, paper, or scissors
and the computer will respond with a choice of its own
via the random module.
"""

# Importing necessary libraries
import random
import sys

def check(userInput, comInput): # This function compares two choices, determines the winner
    # Utilizing a pseudo-switch case
    switch = {
        1: "Rock",
        2: "Paper",
        3: "Scissors",
    }

    choice1 = switch[userInput]
    choice2 = switch[comInput]

    # If-elif block to compare choices
    if (choice1 == "Rock" and choice2 == "Paper") or (choice1 == "Paper" and choice2 == "Scissors") or (choice1 == "Scissors" and choice2 == "Rock"):
        print("Computer Wins!")
    elif (choice1 == "Rock" and choice2 == "Scissors") or (choice1 == "Paper" and choice2 == "Rock") or (choice1 == "Scissors" and choice2 == "Paper"):
        print("You win!")
    else:
        print("It's a tie!")

# Main function to start the game.
# Provides output to terminal and 
# overall "look" to the game.
def runGame():
    print("*** Rock, Paper, Scissors! *** \n     Ready to Play? (y/n)")
    ans = input() # Storing user's choice whether to start the game or not
    
    # Logic for user's choice
    if(ans == "n"):
        sys.exit("Bye!")
    elif(ans == "y"):
        startGame()
    else:
        print("Sorry, that wasn't a valid choice!")
        runGame() # recursive call to reprompt the user again

# Function to actually play the game
def startGame():
    gameStatus = True # Variable to control the game's active status

    while gameStatus:
        print("\tMake your choice! \n\tRock (1)\n\tPaper (2)\n\tScissors (3)")
        userChoice = input()
        try: # Test to make sure input is valid
            choice = int(userChoice)
            if choice <= 0 or choice > 3:
                print("Sorry, that wasn't an option!")
                startGame()
            else:
                computerChoice = random.randint(1,3)
                check(choice,computerChoice)
        except:
            print("Sorry, that was an invalid input!")
            startGame()

        # Code block below this comment should always display after each round
        print("Play again? (y/n)")
        ans = input()
        if ans == "y":
            startGame()
        elif ans == "n":
            gameStatus = False
            sys.exit("Thanks for playing!")
        else:
            print("Sorry, that wasn't a valid choice!")
            startGame()


# Running the program
runGame()