import random


# Winning ASCII Design
def you_win():
    print('''
     /$$     /$$ /$$$$$$  /$$   /$$       /$$      /$$ /$$$$$$ /$$   /$$
    |  $$   /$$//$$__  $$| $$  | $$      | $$  /$ | $$|_  $$_/| $$$ | $$
     \  $$ /$$/| $$  \ $$| $$  | $$      | $$ /$$$| $$  | $$  | $$$$| $$
      \  $$$$/ | $$  | $$| $$  | $$      | $$/$$ $$ $$  | $$  | $$ $$ $$
       \  $$/  | $$  | $$| $$  | $$      | $$$$_  $$$$  | $$  | $$  $$$$
        | $$   | $$  | $$| $$  | $$      | $$$/ \  $$$  | $$  | $$\  $$$
        | $$   |  $$$$$$/|  $$$$$$/      | $$/   \  $$ /$$$$$$| $$ \  $$
        |__/    \______/  \______/       |__/     \__/|______/|__/  \__/
        ''')


# Start of game print-outs
def start_prints():
    print("Let's play Battleship!")
    print('''
                                                      _     
                                              /    _,'|     
                                             /_ _,'   |     
                                            $$;'     _;     
                            ,-'-._    ,-'. ,-'    _.'
                            \     `-,'  ,-'    _,'
           _od8PP8booo   ,....       ;,'    ,,'  _____
         d8P''         ,'     \   _,'    ,-' ,oo8P"""Y8.
         `'             `-.    i,'    ,-',odPP''      8b
                           `-,'    ,-',o8P'          ,8P
                        .',-'   ,-',o8P'             d8
                     .'.-'  _,-',o8P'               ,8P
                   ',-'  _,' _o8P'                  dP
        8bo,     _,'  _,'  ,dP'                    d8
          Y8'    \ ,,'  ,o8P'                    _op'                     _,d8P
          dP      '  ,o8P'                     ,o8'                   ,oo8P"'
          Yb     _oo8P'                      ,dP'                 ,odPP''
           Ybooo8P''                       ,dP'              _,odPP'
             ''                           o8'            _oo8P"'
                                        ,8P         _,odPP''
                                       d8'    __,odPP"'
                                       Y8oooo8PP"'
                                        ~~~~~~
        ''')
    print("You have 3 Turns. Locate the Enemy ship by guessing in which column and row it is, number from 1 to 5")


# Stored game code in def for easy new game looping
def game_code():
    # Board set inside game_code to reset if new game is set
    board = []
    for i in range(5):
        board.append(["O"] * 5)

    # Print the game board
    def print_board(board):
        for row in board:
            print(" ".join(row))

    start_prints()
    # Generate a random location for the ship
    ship_row = random.randint(0, len(board) - 1)
    ship_col = random.randint(0, len(board[0]) - 1)

    print_board(board)
    # Loop through the game while the user has valid turns
    turn_phase = 1
    while turn_phase < 4:

        while True:
            try:
                if turn_phase < 3:
                    print("Turn " + str(turn_phase))
                    guess_row = (int(input("Guess Row:"))) - 1
                    guess_col = (int(input("Guess Col:"))) - 1
                    break
                elif turn_phase == 3:
                    print("Turn " + str(turn_phase) + " LAST CHANCE!!!!")
                    guess_row = (int(input("Guess Row:"))) - 1
                    guess_col = (int(input("Guess Col:"))) - 1
                    break
                else:
                    guess_row = (int(input("Guess Row:"))) - 1
                    guess_col = (int(input("Guess Col:"))) - 1
                    break
            except ValueError:
                print("Input only one number from 1 to 5")

        # Check if the guess is correct
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            you_win()
            break
        else:
            # Check if the guess is on the board
            if guess_row not in range(5) or \
                    guess_col not in range(5):
                print("Oops, that's not even in the ocean. Try Again!")
                print("Input only one number from 1 to 5")

            # Check if the guess has already been made
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already. Try Again!")

            # Check if the ship was missed and add turn counter
            else:
                print("You missed my battleship!")
                turn_phase = turn_phase + 1
                board[guess_row][guess_col] = "X"
            # Print the updated game board
            print_board(board)

        # If the player has used all turns
        if turn_phase == 4:
            print("Game Over")
            print(f"The battleship was located at row {ship_row + 1}, col {ship_col + 1}")


def new_game_exit_loop():
    # After Game options to Restart game or exit
    new_game = (str(input("Do you want to play another game? press Y for yes or N for NO  "))).upper()

    while new_game not in ("Y", "N"):
        print("Not a Valid Input!!")
        new_game = (str(input("If you want to play another game press Y for yes or N for NO  "))).upper()

    if new_game == "Y":
        game_code()
        new_game_exit_loop()
    else:
        print("Thanks for playing!")
        exit()


game_code()

new_game_exit_loop()
