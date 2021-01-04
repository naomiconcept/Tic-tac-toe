# to make this game we will need:
# a board: display this board,
#  a function: to play the game,
#  a function: to check win: check rows, check columns
# a function: to check tie
# flip player

# Introduction
print("Hello! \nWelcome to games by NaomiConcept ^-^") # or you could just put any random name to bring your code alive, lol.

# =======================Global Variables ========================

# if game is still going
game_still_going = True


# who won? or tie?
winner = None

# whose turn is it?
current_player = "x"
######################################################################## all these above are global variables, you can try look up what global variable is on Google.

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-" ]

# function to display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# function to start the gameeeee
def play_game():

    # display board game
    display_board()

    # while the game is still going 
    while game_still_going:

       # to choose position of choice from the player
      handle_turn(current_player)

       # check if the game has ended
      check_if_game_over()

      # flip to the other player  
      flip_player()

    # the game has ended here
    if winner == "x" or winner == "o":
        print(winner + " won!")
    elif winner == None:
        print("Tie!")


# function to choose position of choice from  player on the board
def handle_turn(player):
    #global player

    print(player + "'s turn.")
    position = input("choose a position from 1-9: ")

    valid = False
    while not valid:

     while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose a position from 1-9: ")


     position = int(position) - 1


     if board[position] == "-":
         valid = True
     else:
        print("You cant go there, Go again.")


    board[position] = player

    display_board()


    # function to check if game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


    #function to check for winner
def check_for_winner():

    # set up global variables
    global winner

    # check rows
    row_winner = check_rows()

    # check columns 
    colum_winner = check_colums()  
    
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there is a win
        winner = row_winner

    elif diagonal_winner:
        # there is a win
        winner = diagonal_winner

    elif colum_winner:
        # there is a win
        winner = colum_winner

    else:
        # no win
        winner = None
        
    return

# a function to check rows for wins
def check_rows():
    # set up global variables
    global game_still_going

    # checking the rows if they are the same
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    
    # return the winner(x or o)
    if row_1:
        return board[0]

    elif row_2:
        return board[3]

    elif row_3:
        return board[6]

    return


def check_diagonals():
    # set up global variables
    global game_still_going

    # checking if digonals are they are the same
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    # return the winner(x or o)
    if diagonal_1:
        return board[0]

    elif diagonal_2:
        return board[6] 

    return


def check_colums():
    # set up global variables
    global game_still_going

    # checking if digonals are they are the same
    colum_1 = board[0] == board[3] == board[6] != "-"
    colum_2 = board[1] == board[4] == board[7] != "-"
    colum_3 = board[2] == board[5] == board[8] != "-"

    if colum_1 or colum_2 or colum_3:
        game_still_going = False

    # return the winner(x or o) 
    if colum_1:
        return board[0]

    elif colum_2:
        return board[1]

    elif colum_3:
        return board[2] 

    return


def check_if_tie():
    # declaring game still going
    global game_still_going

    if "-" not in board:
        game_still_going = False
    
    return


def flip_player():
    # global variables we need
    global current_player

    # if the current player was x, then change it o
    if current_player == "x":
        current_player = "o"

    # if the current player was x, then change it o
    elif current_player == "o":
        current_player = "x"
    return

play_game()







