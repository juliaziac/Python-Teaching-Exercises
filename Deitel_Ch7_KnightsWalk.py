import numpy as np
import pandas as pd
import random

#### Create board ####
print('\n')
array = np.zeros((8, 8), dtype=int)
board = pd.DataFrame(array)
print(board.to_string(header = False, index = False, col_space = 2))
print('This is a blank board.\n')

#### Start knight at random position ####
knight_row = random.randint(0, 7)
knight_col = random.randint(0, 7)
board.at[knight_row, knight_col] = 1
counter = 1
print(board.to_string(header = False, index = False, col_space = 2))
print(f'As seen above, Knight is at ({str(knight_col)}, {str(knight_row)}).\n')

#### Function for each move (8 possible) ####
def move_1(knight_row, knight_col):
    knight_row -= 1
    knight_col += 2
    return (knight_row, knight_col)
def move_2(knight_row, knight_col):
    knight_row -= 2
    knight_col += 1
    return (knight_row, knight_col)
def move_3(knight_row, knight_col):
    knight_row -= 2
    knight_col -= 1
    return (knight_row, knight_col)
def move_4(knight_row, knight_col):
    knight_row -= 1
    knight_col -= 2
    return (knight_row, knight_col)
def move_5(knight_row, knight_col):
    knight_row += 1
    knight_col -= 2
    return (knight_row, knight_col)
def move_6(knight_row, knight_col):
    knight_row += 2
    knight_col -= 1
    return (knight_row, knight_col)
def move_7(knight_row, knight_col):
    knight_row += 2
    knight_col += 1
    return (knight_row, knight_col)
def move_8(knight_row, knight_col):
    knight_row += 1
    knight_col += 2
    return (knight_row, knight_col)

#### Choose a move at random ####
moves = [move_1, move_2, move_3, move_4, move_5, move_6, move_7, move_8]
while counter < 64:
    if len(moves) == 0:
        print(f'The Knight got stuck after move {counter}.\n')
        break

    else:
        chosen_move = moves.pop(random.randint(0, len(moves)-1))
        new_knight_row, new_knight_col = chosen_move(knight_row, knight_col)

        #### Check if that move is on the board ####
        if new_knight_row > 7 or new_knight_col > 7 or new_knight_row < 0 or new_knight_col < 0:
            continue

        #### Check if that spot has already been occupied ####
        if board.at[new_knight_row, new_knight_col] != 0:
            continue

        #### If valid, update board to put counter nubmer at that spot, reset moves list ####
        moves = [move_1, move_2, move_3, move_4, move_5, move_6, move_7, move_8]
        knight_row, knight_col = new_knight_row, new_knight_col
        counter += 1
        board.at[knight_row, knight_col] = counter
        print(board.to_string(header = False, index = False, col_space = 2))
        print(f'As seen above, Knight is at ({str(knight_col)}, {str(knight_row)}).\n')

# Next idea: backtracking search