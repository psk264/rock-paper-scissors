# game-with-gui.py
# Rock-Paper-Scissors program executed from GUI
# Adapted from prof-rossetti repository: https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/pysimplegui.md

#import modules to use additional third party packages 
import random
from PySimpleGUI.PySimpleGUI import OK
import PySimpleGUI as sg


def gamelogic_return_code(user_choice, computer_choice) -> int:
    if(user_choice in valid_options): 
     #   print("Computer's choice:", computer_choice)
        if(user_choice == computer_choice):
            # print("Its a tie!")
            return 0
        elif(user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
       #     print(f"{player_name} won! {user_choice} beats {computer_choice}")
            return 1
        else:   
            return 2 
            # print("Oh, the computer won. It's ok.")
        # print("Thanks for playing. Please play again!")

    else:
        # print("Oops, invalid input. Accepted values:'rock', 'paper', 'scissors'. You entered '",user_choice,"'")
        # print("THIS IS THE END OF OUR GAME. PLEASE TRY AGAIN.")
        return 5

valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options) 

layout_initial = [
    [sg.Text("Enter your name: "), sg.InputText()],
    [sg.Button("Play")]
]

window = sg.Window("Rock-Paper-Scissors").Layout(layout_initial)
event, values = window.Read()

player_name = values[0] 
layout_game = [
    [sg.Text("Welcome, "+ player_name+"! Let's Play.")],
    [sg.Text("Please enter your choice: "), sg.InputText()],
    # [sg.Text("Computer's choice: "+ computer_choice)],
    [sg.OK()]
]

if event == "Play":
    window.close()
    window_game = sg.Window("Game - window").Layout(layout_game)
    button, values = window_game.Read()
    # sg.popup(window_game)
    player_choice = values[0]

gamelogic_return_code = gamelogic_return_code(player_choice, computer_choice)

if(gamelogic_return_code == 0):
    sg.popup("Its a Tie! Please try again!")
elif(gamelogic_return_code == 1): 
    sg.popup("Congratulations! You won! \n" + player_name + "'s choice: " + player_choice + " beats Computer's choice: " + computer_choice)
elif(gamelogic_return_code == 2):
    sg.popup("Oh, the computer won. \n" + "Computer choice: " + computer_choice + " beats " + player_name + "'s choice " + player_choice +". \nIt's ok. Thanks for playing. Please play again!")
else:
    sg.popup("Oops, invalid input. \nAccepted values :'rock', 'paper', 'scissors'. \nYou entered:  '" + player_choice + 
            "'\nTHIS IS THE END OF OUR GAME. PLEASE TRY AGAIN.")    
    sg.OK()