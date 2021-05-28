# rock-paper-scissors-exercise
Assignment 1 - rock paper scissors exercise

## Objective
This repo holds the code for the game of rock-paper-scissors :black_circle: x :page_facing_up: x :scissors:.  Wanna play? Please continue reading :) 

## Instructions
1. Use git client to clone or download this remote repository, [rock-paper-scissors-exercise](https://github.com/psk264/rock-paper-scissors-exercise), on your local machine.  Note the location where it is cloned or downloaded
2. Use command line application to navigate to the location where this repository was cloned or downloaded.  Ensure that <base> from conda initialization is shown on cmd line.  If <base> is not shown then, before proceeding, run command:
 ```conda init bash```
3. Since this code uses specific packages like python-dotenv, it is recommended to create a new project specific anaconda virtual environment using following command:
``` conda create -n rpc-game-env python=3.8```
4. Activate the Anaconda environment "rpc-game-env" using the command:
```conda activate rpc-game-env```
5. After virtual environment is active i.e. <rpc-game-env> is shown on command-line, then install the third-party package python-dotenv on this virtual environment using command:
```pip install -r requirement.txt```
**Note:** The requirements.txt file is already provided in the repository.
6. After the setup is complete, execute and start the game using command:
```python game.py```

## Additional Information
* The game.py code file demostrate 3 different approaches to get player name
  * 1. Taking the player name as input from command line
  * 2. Reading the player name from env file
  * 3. Reading the player name from the command line using env (by importing os package)
* The game.py code file demostrate 2 different approached to game logic
  * 1. Seperate if-elif blocks
  * 2. Single if-elif-else block 


## Details of how this repo came to be 
(**Note - I understand this should not be part of readme but I wanted to document the steps when we did this exercise during class for future referenc**)
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
