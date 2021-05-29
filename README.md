# Rock-Paper-Scissors-Exercise
Assignment 1 - rock paper scissors exercise

## Prerequisite
* Anaconda 3.7+
* Python 3.7+
* Pip
* Git Bash

## Objective
This repo holds the code for the game of rock-paper-scissors :black_circle: x :page_facing_up: x :scissors:.  
**Wanna play?** Please continue reading :) 

There are 2 ways to play this game!  To play using command line please use the script file [**_game.py_**](https://github.com/psk264/rock-paper-scissors-exercise/blob/main/game.py) and to play using GUI use the script file [**_game-with-gui.py_**](https://github.com/psk264/rock-paper-scissors-exercise/blob/main/game-with-gui.py) in following instructions. 

## Instructions
1. Use git client to clone or download this remote repository, [rock-paper-scissors-exercise](https://github.com/psk264/rock-paper-scissors-exercise), on your local machine.  Note the location where it is cloned or downloaded
2. Use command line application to navigate to the location where this repository was cloned or downloaded.  Ensure that ``<base>`` from conda initialization is shown on cmd line.  If ``<base>`` is not shown then, before proceeding, run command:<br/>
```conda init bash```
3. Since this code uses specific packages like python-dotenv, it is recommended to create a new project specific anaconda virtual environment. Here we create virtual environment name "rpc-game-env" using following command.  To create a environment with a different name, simply replace rpc-game-env with desired name:<br/>
``` conda create -n rpc-game-env python=3.8```
4. Activate the Anaconda environment "rpc-game-env" using the command:<br/>
```conda activate rpc-game-env```
5. After virtual environment is active i.e. ``<rpc-game-env>`` is shown on command-line, then install the third-party package python-dotenv on this virtual environment using command:<br/>
 ```pip install -r requirements.txt```<br/>
**NOTE:** The requirements.txt file is already provided in the repository.
6. After the setup is complete, depending on your preference to play using command line or GUI execute and start the game using one of the following commands:<br/>
Play using command prompt:  ```python game.py```   
Play using GUI:  ```python game-with-gui.py```  <br/>  

**NOTE:** Depending on which approach is commented out on the game.py, the script will either ask for player name on command line or read "Jane Doe" from .env file. Details about different approaches are listed below. 

## Additional Information
* The game.py code file demostrate 3 different approaches to get player name
  1. Taking the player name as input from command line
  2. Reading the player name from env file
  3. Reading the player name from the command line using env (by importing os package)
* The game.py code file demostrate 2 different approached to game logic
  1. Seperate if-elif blocks
  2. Single if-elif-else block 
* A separate script file named game-with-gui.py has the code to play this game from GUI. To run the GUI mode, please follow same steps as above but substitute game.py with game-with-gui.py

## END OF README 

(**Note to Professor - I understand this should not be part of readme but I wanted to document the steps when we did this exercise during class for future referenc**)
### This block can be ignored: Details of how this repo came to be 
commit 1 - setup repo
* _step 1: Create repo on github_
* _step 2: Clone it locally_
* _step 3: (only on my machine) add desktop.ini to gitignore_
* _step 4: create game.py file with code_
* _step 5: create container on using anaconda_
* _step 6: activate container_
* _step 7: run python game.py_
* _step 8: commit the changes to github_
* _step 9: push the changes to origin so its uploaded on the remote repository_

commit 2 - capture user input
* _step 10: update game.py file to use functions like print and input_
* _step 11: using command line, run python game.py to ensure its working successfully_
* _step 12: commit the changes to github_
* _step 13: push the changes to origin so its uploaded on the remote repository_

commit 3 - validate user input
* _step 14: create conditional statement block to check for valid input using if-else statement_
* _step 15: commit the changes to github_
* _step 16: push the changes to origin so its uploaded on the remote repository_

commit 4 - random choice for player 2 - computer
* _step 17: user a random module to use choice function in random module.  User import statement to import random._
* _step 18: Use list to store valid option_
* _step 19: commit the changes to github_
* _step 20: push the changes to origin so its uploaded on the remote repository_

commit 5 - game logic using if- elif
* _step 21: Added the game logic using if - elseif block_
* _step 22: commit the changes to github_
* _step 23: push the changes to origin so its uploaded on the remote repository_
