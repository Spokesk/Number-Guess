"""Number Guess

Discription: Number guessing game, generates random integer, stores, and
prompts User to guess an integer.  If matching congratulates and terminates.
If not advises player of difference of their guessed integer. 
Now with multiple difficulties!

https://www.learnpython.org/en/String_Formatting
https://realpython.com/python-string-formatting/
name = "neo"
f'Hello, {name}'

Author: Kesk

"""

# https://docs.python.org/3/library/sys.html
import sys
from random import randint

maxInt = 0
choosenInt = 0 
guessedInt = 0

difficultySelect = ['Easy', 'Vanilla', 'GRISLEY', 'Custom']

playAgainResponse = ['Yes','No']

def playAgain():
    
    playAgainAnswer = input("Wanna play again kiddo? Yes/No ").lower().capitalize()
    while True:
        if playAgainAnswer == 'Yes':
            print("kk ;D")
            start()
        elif playAgainAnswer == 'No':
            print("bye by boy")
            sys.exit()
       
# TODO Quickly intergrate 'custom' difficulty 
def custom():
    while True:
        try:
             maxInt = int(input("Choose an upper limit :D "))
             break
        except:
            print("That ain't a fair answer kid :/")
            continue

    # Choosing random number from user defined limit
    choosenInt = randint(0, maxInt)
    while True:
        try:
            guessedInt = int(input("Kk, I've choosen gimmie your best shot! "))
        except:
            print("That ain't a fair answer kid :/")
            continue

        if 0 > guessedInt or guessedInt > 5:
            print("Not within the range :/")  
        elif guessedInt > choosenInt:
            print("liiiiiitle high there bud")
        elif guessedInt < choosenInt:
            print("low balling it there ma'dude")  
        else:
            print("you are a Woinner")
            playAgain()   
    
# TODO Create 'Easy' difficulty, integer list of numbers 1-5
def easy():
 
    print("Easy selected!") 

    choosenInt = randint(0,5)

    while True:
        try:
            guessedInt = int(input("Kk, I've choosen gimmie your best shot! "))
        except:
            print("That ain't a fair answer kid :/")
            continue

        if 0 > guessedInt or guessedInt > 5:
            print("Not within the range :/")  
        elif guessedInt > choosenInt:
            print("liiiiiitle high there bud")
        elif guessedInt < choosenInt:
            print("low balling it there ma'dude")  
        else:
            print("you are a Woinner")   
            playAgain()   

# TODO Create 'Vanilla' difficulty, integer list of numbers 1-12
def vanilla():
 
    print("Vanilla selected!") 

    choosenInt = randint(0,12)

    while True:
        try:
            guessedInt = int(input("Kk, I've choosen gimmie your best shot! "))
        except:
            print("That ain't a fair answer kid :/")
            continue

        if 0 > guessedInt or guessedInt > 5:
            print("Not within the range :/")  
        elif guessedInt > choosenInt:
            print("liiiiiitle high there bud")
        elif guessedInt < choosenInt:
            print("low balling it there ma'dude")  
        else:
            print("you are a Woinner")   
            playAgain()   

# TODO Create 'GRISLEY' difficulty, integer list of numbers 1-100
def grisley():
 
    print("GRISLEY selected!") 

    choosenInt = randint(0,100)

    while True:
        try:
            guessedInt = int(input("Kk, I've choosen gimmie your best shot! "))
        except:
            print("That ain't a fair answer kid :/")
            continue

        if 0 > guessedInt or guessedInt > 5:
            print("Not within the range :/")  
        elif guessedInt > choosenInt:
            print("liiiiiitle high there bud")
        elif guessedInt < choosenInt:
            print("low balling it there ma'dude")  
        else:
            print("you are a Woinner")    
            playAgain()   

                           

# Initial difficulty select input prompt
    # TODO Create difficulty name list, numbers(?) to call on, name after functions
    #       four uin total, easy, vanilla, GRISLEY, and custom, custom function done
    #      also have brief discription of each difficulty too


def start():
    # Start up message
    print("Let's play squire!")

    difficultyChoice = input("""Choose a difficulty: 
    Easy - (0-5)
    Vanilla - (0-12)
    GRISLEY - (0-100)
    Custom - You decide!
    """).lower().capitalize()

    while True:

        if difficultyChoice == 'Easy':
            print("Kk babay steps!")
            easy()

        elif difficultyChoice == 'Vanilla':
            print("AHHHH! White bread!")
            vanilla()

        elif difficultyChoice == 'GRISLEY!':
            print("Getting HARDCORE, RIP AND TEAR")  
            grisley()  

        elif difficultyChoice == 'Custom':
            print("Bring your own number!")
            custom()

        else:
            print("Answer me properly Boi")   

start()