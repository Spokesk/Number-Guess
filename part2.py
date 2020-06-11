# Import integers from the random function
from random import randint

# Define guessedInt and generatedInt to 0
guessedInt = 0

# Generate random integer, 'generatedInt', between 0 and a 10.
generatedInt = randint(0,10)

# Print to communicate this.
print("I'm thinking....")

# Prompt user to guess integer
try:
    guessedInt = int(input("kk your guess babes ;) (it's between 0-10) "))
except:
    print("Nah you big ninny, BETWEEN 0-10 HINTHINTHINT")

# Compare guessedInt with generatedInt, check if greater then above or below specified boundries
 if guessedInt > 10 or guessedInt < 0:
    print("Nah CHOOSE a number BETWEEN 0-10")

# Compare guessedInt with generatedInt, check for > then range.
elif guessedInt > generatedInt:
    print("Too big guv'na")

# Compare guessedInt with generatedInt, check for < then range. 
elif guessedInt < generatedInt:
    print("Too looooooow")

# Implied logic is equalisation.
else:
    print("Yeah first try, nice one bud!")