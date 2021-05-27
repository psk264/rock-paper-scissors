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
if(user_choice in valid_options):
    # print("VALID.KEEP GOING")
    if(user_choice == computer_choice):
        print("Its a tie!")
    elif(user_choice == "rock"):
        if(computer_choice == "scissors"):
                print(player_name, "wins!")
        elif(computer_choice == "paper"):
                print("Oh, the computer won. It's ok.")
    elif(user_choice == "paper"):
        if(computer_choice == "rock"):
                print(player_name, "wins!")
        elif(computer_choice == "scissors"):
                print("Oh, the computer won. It's ok.")
    elif(user_choice == "scissors"):
        if(computer_choice == "paper"):
                print(player_name, "wins!")
        elif(computer_choice == "rock"):
                print("Oh, the computer won. It's ok.")
    print("Thanks for playing. Please play again!")
else:
    print("Oops, invalid input. Accepted values:'rock', 'paper', 'scissors'. You entered '",user_choice,"'")
    print("THIS IS THE END OF OUR GAME. PLEASE TRY AGAIN.")
    exit()


