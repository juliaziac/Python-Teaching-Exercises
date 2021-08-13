import Deitel_Ch7_KnightsWalk_function

# see if counter ever reaches 64

highest_move = 0
num_moves = 100000
for i in range(num_moves):
    new_move = Deitel_Ch7_KnightsWalk_function.KnightsWalk()
    if new_move > highest_move:
        highest_move = new_move
print(f'\nAfter {num_moves} moves, your highest move is {highest_move}.\n')
