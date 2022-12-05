import numpy as np
#9, 53
#3, 6

file = open('day_5_data.txt')
crates = np.empty((9,53), dtype = str)
num_crates = np.zeros(9, dtype=int)

for line in file:
    if line == '\n':
        break
    for column in range(9):
        if line[4*column+1].isalpha():
            crates[column][num_crates[column]] = line[4*column+1]
            num_crates[column] += 1

for column in range(9):
   crates[column][0:num_crates[column]] = np.flip( crates[column][0:num_crates[column]] )

moves = np.empty((0,3), dtype=int)

for line in file:
    command = line.replace('move ', '').replace('from ', '').replace('to ', '').strip('\n')
    command = list(map(int, command.split(' ')))
    moves = np.append(moves, [command], axis=0)

for com in moves:
    amount = com[0]
    f_col = com[1] - 1
    t_col = com[2] - 1

    #crates[t_col][num_crates[t_col]:num_crates[t_col]+amount] = np.flip(crates[f_col][num_crates[f_col]-amount:num_crates[f_col]]) # THIS IS FOR ASSIGNMENT 1
    crates[t_col][num_crates[t_col]:num_crates[t_col]+amount] = crates[f_col][num_crates[f_col]-amount:num_crates[f_col]] # THIS IS FOR ASSIGNMENT 2
    crates[f_col][num_crates[f_col]-amount:num_crates[f_col]] = np.empty(amount, dtype=str)

    num_crates[t_col] += amount
    num_crates[f_col] -= amount

print(crates)