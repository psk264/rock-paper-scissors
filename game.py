# game.py

#import modules to use additional modules
import random

#Input command variation, using print and input 
# print("Enter your name: ")
# player_name = input()

#Above statements can be reduced to single line of code
player_name = input("Enter your name: ")

#User Choice:
print("Welcome, ", player_name, "! Get ready to play Rock-Paper-Scissors.")
user_choice = input("Please chose one of 'rock', 'paper', 'scissors': ")
print(player_name,"'s choice:", user_choice)

#Computer Choice:
# one way to write the choice statement is to enter the list in the argument
# computer_choice = random.choice(["rock","paper","scissors"]) 

#another way to write choice statement using list
valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options) 

print("Computer's choice:", computer_choice)

#Game Logic
if(user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID.KEEP GOING")
else:
    print("Oops, invalid input. Accepted values:'rock', 'paper', 'scissors'. You entered '",user_choice,"'")
    print("THIS IS THE END OF OUR GAME. PLEASE TRY AGAIN.")
    exit()


