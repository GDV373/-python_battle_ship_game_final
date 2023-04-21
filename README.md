# **Battle Ship Game**

For my third Portfolio Project submitted as part of the Code Institute's Diploma in full-stack software development course, I created a board game, commonly known as battleship, called ' Battle ship game'. This is a Python terminal please follow the deployment content to run this game as currently Heroku is not working propperly.  


- To view the repository on Github **[Click Here](https://github.com/GDV373/Python_Battle_Ship_Game)**.


## **Summary**
  This interactive game provides users with an easy way to 'fire cannonballs' at a computer ‘enemy’s fleet of ships’. The game is based on the well-known board game ‘Battleship’, to learn more about this game **[Click Here]( https://en.wikipedia.org/wiki/Battleship_game)**.



## **[Contents](#contents)**

1.	**[How to Play](#how-to-play)**
2.	**[Features](#features)**
3.	**[Features Left to Implement](#features-left-to-implement)**
4.	**[Data Model](#data-model)**
5.	**[Testing](#testing)**
6.	**[Bugs](#bugs)**
7.	**[Deployment](#deployment)**
8.	**[Acknowledgements](#acknowledgements)** 

## **[How to Play](#how-to-play)**

In this version of the classic Battleship game, one randomly located ship is generated which the player cannot see. 

The player must guess the coordinates of the hidden ships by choosing a row number and a column number. The player has 3 ‘cannonballs’ or turns to take in order to ‘hit’ the hidden ships. 

Missis are indicted by ‘X’ or the game ends with a you win ASCII art if you hit and win. 

If the player hits the computer’s ships they win the game. If they fire all of their cannonballs and fail to do so, they lose the game.  

## **[Features](#features)**

### Existing features
* Random board generation
  * Ships are randomly placed on the board by the computer so that the player cannot see where they are.

![Screenshot of herokus error](/assets/images/Screenshot-battle-ship-start-game.png "Screenshot of heroku`s error")<br> 

* Accepts player’s input.

* Validates coordinates input by player.

* Tells player if they input invalid values or the same values more than once without loosing the turn.

* Tells player how many turns or 'cannon balls' they have left.

![Screenshot of herokus error](/assets/images/Screenshot-battle-ship-3-turns.png "Screenshot of heroku`s error")<br> 

* Able to reply the game without runnning the script again.

![Screenshot of herokus error](/assets/images/Screenshot-battle-ship-you-win.png "Screenshot of heroku`s error")<br> 

### **[Featuers left to implement](#features-left-to-implement)**

 * Add more ship for harder difficulty
 * An option for the User to decide on the size of the game board

## **[Data Model](#data-model)**

-	Functions are used on throughout the code to avoid repetitive code as much as possible.

-	The random Method was imported to generate the ships locations on the game board.  


## **[Testing](#testing)**

The code was built and tested using PyCharm using it to ensure there were no errors present, such as issues with indentation or whitespaces.

![Screenshot of herokus error](/assets/images/PyCharm-errors-and-warnings.png "Screenshot of heroku`s error")<br> 

## **[Bugs](#bugs)**

One bugs were encountered in developing this project:

-       Game would not loop more than one time because of missing line. This was later added after further testing of the game in the def new_game_exit_loop(): where it needed to run again if player was to play more than 2 games.


‘Bugged’ code: 

~~~

def new_game_exit_loop():
    # After Game options to Restart game or exit
    new_game = (str(input("Do you want to play another game? press Y for yes or N for NO  "))).upper()

    while new_game not in ("Y", "N"):
        print("Not a Valid Input!!")
        new_game = (str(input("If you want to play another game press Y for yes or N for NO  "))).upper()

    if new_game == "Y":
        game_code()

    else:
        print("Thanks for playing!")
        exit()
~~~

debugged code:

~~~
def new_game_exit_loop():
    # After Game options to Restart game or exit
    new_game = (str(input("Do you want to play another game? press Y for yes or N for NO  "))).upper()

    while new_game not in ("Y", "N"):
        print("Not a Valid Input!!")
        new_game = (str(input("If you want to play another game press Y for yes or N for NO  "))).upper()

    if new_game == "Y":
        game_code()
        
    else:
        print("Thanks for playing!")
        exit()
~~~

##	**[Deployment](#deployment)**

**Heroku**

![Screenshot of herokus error](/assets/images/Screenshot_error_heroku.png "Screenshot of heroku`s error")<br> 

Currently Heroku is not working propperly please follow the solution below to run the python game on a python web browser compiler

1. copy the raw code from git link here > **[Click Here](https://raw.githubusercontent.com/GDV373/Python_Battle_Ship_Game/main/Battle_Ship_Game.py)**
2. Open the website compiler by clicking this link > **[Click Here](https://www.programiz.com/python-programming/online-compiler/)**
3. Paste the raw code into the main.py area on the left side.
4. Press the Blue Run button and play the game from the right side in the Shell area.


##	**[Acknowledgements](#acknowledgements)** 

- My mentor, Brian Macharia, for the great support and ideas while doing the project.  
   
  

**[Click Here](#contents)** to return to Contents
