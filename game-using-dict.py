import random
import os
import dotenv

#Input command variation, using print and input 
# print("Enter your name: ")
# player_name = input()

#Above statements can be reduced to single line of code
#Option 1:
print("Fetching player name from command line")
player_name = input("Enter your name: ")

#Option 2: Fetching player name from command line using command: PLAYER_NAME="Guest" if env is missing (package needed: os)
# PLAYER_NAME = os.getenv("PLAYER_NAME")
# player_name = PLAYER_NAME
# print("Fetching player name from command line using command \'PLAYER_NAME=\"Guest\" python game.py\'")


#Option 3:Fetching player name from environment variable (package needed: dotenv)
# dotenv.load_dotenv()
# player_name = os.getenv("PLAYER_NAME")
# print("Fetching player name from env file")


#User Choice:
if(player_name and player_name.strip()):
    print("Welcome, ", player_name, "! Get ready to play Rock-Paper-Scissors.")
else:
    print("OOPS! player name is empty.  No problem, we got your back!")
    player_name = input("Please enter the player name: ")
user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(player_name+"'s choice:", user_choice)

#Computer Choice:
# one way to write the choice statement is to enter the list in the argument
# computer_choice = random.choice(["rock","paper","scissors"]) 

#another way to write choice statement using list
valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options) 
# print("Computer's choice:", computer_choice)

winners = {
    "rock": {
        "rock": None,
        "paper": "paper",
        "scissors": "scissors"
    },
    "paper": {
        "rock": "rock",
        "paper": None,
        "scissors": "scissors"
    },
     "scissors": {
        "rock": "rock",
        "paper": "paper",
        "scissors": None
    }
}

winner = winners[user_choice][computer_choice]
if winner == user_choice:
    print(f"{player_name} won! {user_choice} beats {computer_choice}")
elif winner == computer_choice:
    print(f"Oh, the computer won! {computer_choice} beats {user_choice}")
    print("It's ok")
else:
    print("Its a tie!")
