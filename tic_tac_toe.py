# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)
grid = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]



def start_game(grid):
    def display_board(grid):
        for row in grid:
            print ((" ".join(row)))

    display_board(grid)


# Function for... (choosing a player?)
    current_player = "player1"

    def switch_players(cur_player):
        if cur_player == "player1":
            cur_player = "player2"
            print ("now it's player2 turn")
            return cur_player
        else:
            cur_player = "player1"
            print ("now it's player1 turn")
            return cur_player

# a function to ask the current player to play and store their input
    def ask_input(cur_player):
        if cur_player == "player1":
            input_player1 = input(f" it's your turn x player, please choose a location so: first the line number, then space, then the column ")
            print (input_player1)
            return input_player1
        else:
            input_player2 = input(f" it's your turn o player, please choose a location so: first the line number, then space, then the column ")
            print (input_player2)
            return input_player2

#current_player = switch_players()   
    #input_player = ask_input()

# a function to insert the players input into the grid
    def insert_input(inpt):
        turn_list = inpt.split()
        line = int(turn_list[0])-1
        column = int(turn_list[1])-1
    #print (line, column)
        return[line, column]
    """if player1 == True:
        grid[input_line][input_column] = "x"
    else:
        grid[input_line][input_column] = "0"
    """
# a function that adjusts the grid according to the last move
    def adjust_grid(last_move, cur_player):
        if cur_player == "player1":
            line = last_move[0]
            column = last_move[1]
        #print (f"line: {line}, column: {column}")
            grid[line][column] = "x"
            display_board(grid)
            return grid
        else:
            line = last_move[0]
            column = last_move[1]
        #print (f"line: {line}, column: {column}")
            grid[line][column] = "o"
            display_board(grid)
            return grid


    def another_turn(cur_player):
        input_player = ask_input(cur_player)
        new_move = insert_input(input_player)
        adjust_grid(new_move, cur_player)
        cur_player = switch_players(cur_player)
        return cur_player

    another_turn(current_player)

start_game(grid)

"""
    input_player = ask_input(current_player)
    new_move = insert_input(input_player)
    adjust_grid(new_move, current_player)
    current_player = switch_players(current_player)
    input_player = ask_input(current_player)
    new_move = insert_input(input_player)
    adjust_grid(new_move, current_player)
    current_player = switch_players(current_player)
    """
   

# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
