# Specifing integers as part of the imported random string
from random import randint
# Defining user inputed integer
guessedInt = 6
print ("My guess is... ", guessedInt)
# Specifing range of generated integers
generatedInt = randint(0, 10)
print(generatedInt)
# if/else statments concerning inputed integer
#  to generated integer comaprison
if guessedInt == generatedInt:
    print("YAAAAy A Wonnor iz u!!!1!!!")
elif guessedInt > generatedInt:
    print("to big, sunshine")
else: 
    print("smaller boi, SMALLER!")
     