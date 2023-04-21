# **Battle Ship Game**

For my third Portfolio Project submitted as part of the Code Institute's Diploma in full-stack software development course, I created a board game, commonly known as battleship, called ' Battle ship game'. This is a Python terminal please follow the deployment content to run this game as currently Heroku is not working propperly.  


- To view the repository on Github **[Click Here](https://github.com/GDV373/Python_Battle_Ship_Game)**.

- To view the working python game **[Click Here](https://python-battle-ship.herokuapp.com/)**


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

![Screenshot of battle-ship-start-game](/assets/images/Screenshot-battle-ship-start-game.png "Screenshot of battle-ship-start-game")<br> 

* Accepts player’s input.

* Validates coordinates input by player.

* Tells player if they input invalid values or the same values more than once without loosing the turn.

* Tells player how many turns or 'cannon balls' they have left.

![Screenshot of battle-ship-3-turns](/assets/images/Screenshot-battle-ship-3-turns.png "Screenshot of battle-ship-3-turns")<br> 

* Able to reply the game without runnning the script again.

![Screenshot of battle-ship-you-win](/assets/images/Screenshot-battle-ship-you-win.png "Screenshot of battle-ship-you-win")<br> 

### **[Featuers left to implement](#features-left-to-implement)**

 * Add more ship for harder difficulty
 * An option for the User to decide on the size of the game board

## **[Data Model](#data-model)**

-	Functions are used on throughout the code to avoid repetitive code as much as possible.

-	The random Method was imported to generate the ships locations on the game board.  


## **[Testing](#testing)**

The code was built and tested using PyCharm using it to ensure there were no errors present, such as issues with indentation or whitespaces. Limit of 79 characters per line was used.

![Sreenshot of Pycharm no error](/assets/images/PyCharm-errors-and-warnings.png "Screenshot of Pycharm no error")<br> 

The code was also Validated using CI Python Linter from https://pep8ci.herokuapp.com/. The W605 and W291 warnings are only there beacuse of the ASCCI art. 

![Sreenshot of CI Python Linter No Error page 1](/assets/images/ci-python-linter-p1.png "Sreenshot of CI Python Linter No Error page 1")<br> 

![Sreenshot of CI Python Linter No Error page 2](/assets/images/ci-python-linter-p2.png "Sreenshot of CI Python Linter No Error page 2")<br> 


## Manual Testing

| Test Label             | Test Action                   | Expected Result                                                                                                                                                      | Test Outcome |
|------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Games start load screen         | load screen of ascci art and rules    | The start screen will load the ASCCI art along with the map and the rules of the game.                                                                                                 | PASS         |
| Validate 3 turns           | No more then 3 turns     | The game will only use 3 turns if only 3 new moves are made. If any invalid moves are inputed the turns will not be lost.                                                                                                 | PASS         |
| Validate input for integer values   | Enter non integer value      | The game will tell the user there was an invalid input and print which input was invalid along side the rule.                                                                                 | PASS         |
| Validate input is in available range | Enter number outside range of available row and colloms  | The Game will tell the user an input was out of range.                                                            | PASS         |
| Ask user for input until valid input is entered    | Enter multiple invalid inputs  | The game will tell user that input was invalid before reprinting instructions, options available and prompt user for input again until valid.                         | PASS         |
| Win ASCCI art load    | Showing the ASSCI Art | Loading the ASSCI Art only when user makes correct guess. Tested from all 3 turns and game repeats.                                                                         | PASS         |
| Reply again         | Accepting y or no for new game or exit    | The game accepts capital or non capital "Y" OR "N" to loop into a fresh new game. Any other input is considered invalid input. Game will replay with yes or exit with a thank you note for no.                                                           | PASS         |


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

<details>
    <summary></summary>

* The requirements.txt file in the IDE must be updated to package all dependencies. To do this:
    1. Enter the following into the terminal: 'pip3 freeze > requirements.txt'
    2. Commit the changes and push to GitHub

* Next, follow the steps below:
    1. Login to [Heroku](https://heroku.com/), create an account if necessary
    2. Once at your Dashboard, click 'Create New App'
    3. Enter a name for your application, this must be unique, and select a region
    4. Click 'Create App'
    5. At the Application Configuration page, apply the following to the Settings and Deploy sections:
        * Within 'Settings', scroll down to the Config Vars section to apply the credentials being used by the application. In the Reveal Config Vars enter 'CREDS' for the Key field and paste the all the contents from the creds.json file into the Value field
        * Click 'Add'
        * Add another Config Var with the Key of 'PORT' and the Value of '8000'
        * Within Settings, scroll down to the Buildpacks sections, click to Add a Buildpack
        * Select Python from the pop-up window and Save
        * Add the Node.js Buildpack using the same method
        * Navigate to the Deploy section, select Github as the deployment method, and connect to GitHub when prompted
        * Use your GitHub repository name created for this project
        * Finally, scroll down to and select to deploy 'Automatically' as this will ensure each time you push code in GitHub, the pages through Heroku are updated
    6. Your application can be run from the Application Configuration section, click 'Open App'

</details>

    

***


##	**[Acknowledgements](#acknowledgements)** 

- My mentor, Brian Macharia, for the great support and ideas while doing the project.  
   
  

**[Click Here](#contents)** to return to Contents
