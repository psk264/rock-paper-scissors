# game.py
# Rock-Paper-Scissors program executed from command line

#import modules to use additional third party packages 
import random
import os
import dotenv

#Input command variation, using print and input 
# print("Enter your name: ")
# player_name = input()

#Above statements can be reduced to single line of code
#Option 1:
# print("Fetching player name from command line")
# player_name = input("Enter your name: ")

#Option 2: Fetching player name from command line using command: PLAYER_NAME="Guest" if env is missing (package needed: os)
# PLAYER_NAME = os.getenv("PLAYER_NAME")
# player_name = PLAYER_NAME
# print("Fetching player name from command line using command \'PLAYER_NAME=\"Guest\" python game.py\'")


#Option 3:Fetching player name from environment variable (package needed: dotenv)
dotenv.load_dotenv()
player_name = os.getenv("PLAYER_NAME")
print("Fetching player name from env file")


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

#********************************************************************
#Game Logic Approach 1
#This can be improved by removing duplicate checks and improved readability
#********************************************************************
# if(user_choice in valid_options): 
#     if(user_choice == computer_choice):
#         print("Its a tie!")
#     elif(user_choice == "rock"):
#         if(computer_choice == "scissors"):
#                 print(player_name, "won!")
#         elif(computer_choice == "paper"):
#                 print("Oh, the computer won. It's ok.")
#     elif(user_choice == "paper"):
#         if(computer_choice == "rock"):
#                 print(player_name, "won!")
#         elif(computer_choice == "scissors"):
#                 print("Oh, the computer won. It's ok.")
#     elif(user_choice == "scissors"):
#         if(computer_choice == "paper"):
#                 print(player_name, "won!")
#         elif(computer_choice == "rock"):
#                 print("Oh, the computer won. It's ok.")
#     print("Thanks for playing. Please play again!")

#********************************************************************
#Game Logic Approach 2
#********************************************************************
if(user_choice in valid_options): 
    print("Computer's choice:", computer_choice)
    if(user_choice == computer_choice):
        print("Its a tie!")
    elif(user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print(f"{player_name} won! {user_choice} beats {computer_choice}")
    else:    
        print(f"Oh, the computer won! {computer_choice} beats {user_choice}")
        print("It's ok")
    print("Thanks for playing. Please play again!")

else:
    print("Oops, invalid input. Accepted values: 'rock', 'paper', 'scissors'. You entered '" + user_choice + "'")
    print("THIS IS THE END OF OUR GAME. PLEASE TRY AGAIN.")
    exit()


