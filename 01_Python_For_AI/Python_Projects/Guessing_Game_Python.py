# Guessing game for predicting random number from range 1 to 100

import random

jackpot = random.randint(1,100)
guess = int(input("Guess The Number: "))
counter = 1

while guess != jackpot:
    if guess < jackpot:    
        print("guess Higher")
    else:
        print("guess Lower")  
    guess = int(input("Guess The Number: "))
    counter+=1
      
print("Your Predicted Number is: ", jackpot )  
print("You Took", counter, "Attempts to predict the correct number") 