# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)

# Function for starting the game

def getting_started(board, win=False, cur_player="player1"):
    # a while true loop?
    # this function needs parameters passed? 
    # if the game_ends parameter passed is true, the function breaks
    while win == False:
        display_board(board)
        input_player = ask_input(cur_player)
        move_location = insert_input(input_player)
        placed = adjust_grid(board, move_location, cur_player)
        if not placed:
            continue

        # capture the boolean result from check_for_winner
        win = check_for_winner(board, cur_player)
        if win == True:
            break
        else:
            cur_player = switch_players(cur_player)



# Function for displaying the board
def display_board(board):
    for row in board:
        print ((" ".join(row)))

# Function for asking the input from the player   
def ask_input(cur_player):
    if cur_player == "player1":
        input_player1 = input(f" it's your turn x player, please choose a location so: first the line number, then space, then the column ")
        #print (input_player1)
        return input_player1
    else:
        input_player2 = input(f" it's your turn o player, please choose a location so: first the line number, then space, then the column ")
        #print (input_player2)
        return input_player2

# Function to insert the players input into the grid
def insert_input(input_player):
    turn_list = input_player.split()
    line = int(turn_list[0])-1
    column = int(turn_list[1])-1
    #print (line, column)
    return[line, column]

# Function to adjust the board with the new input
def adjust_grid(board, input_player, cur_player):
    line = input_player[0]
    column = input_player[1]
    
    if board[line][column] != "-":
        print ("this cell is already taken")
        return False
    if cur_player == "player1":
        #print (f"line: {line}, column: {column}")
        board[line][column] = "x"
        display_board(board)
        return board
        
    else:
        #print (f"line: {line}, column: {column}") 
        board[line][column] = "o"
        display_board(board)
        return board
        
    
# Function to switch the players if there no win
def switch_players(cur_player):
        if cur_player == "player1":
            cur_player = "player2"
            print ("now it's player2 turn")
            return cur_player
        elif cur_player == "player2":
            cur_player = "player1"
            print ("now it's player1 turn")
            return cur_player
    
    
# Function to check if theres a win, and if so - who won
def check_for_winner(board, cur_player):
    symbol = "x" if cur_player == "player1" else "o"

    # helper checks all win conditions for the passed symbol
    def check_symbol(sym):
        # rows
        for row in board:
            if all(cell == sym for cell in row):
                return True
        # columns
        for c in range(3):
            if all(board[r][c] == sym for r in range(3)):
                return True
        # diagonals
        if board[0][0] == sym and board[1][1] == sym and board[2][2] == sym:
            return True
        if board[0][2] == sym and board[1][1] == sym and board[2][0] == sym:
            return True
        return False
    win = check_symbol(symbol)
    if win == True:
        print (f"Game over! {cur_player} has won!")
    return win
    
    


    pass
    #if board look such and such, a variable named win should be returned
    # there should be a print "cur_player has won, game is finished"
    # and return the game_ends variable to be used in the 
    # getting started function as True







# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    getting_started(board)
