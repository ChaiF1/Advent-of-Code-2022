import numpy as np

file = open('day_2_data.txt')
data = np.empty((0,2), dtype = str)

for line in file:
    moves = [line.strip('\n').split(' ')]
    data = np.append(data, moves, axis = 0)

scores = {'X': 1, 'A' : 1, 'Y' : 2, 'B' : 2, 'Z' : 3, 'C' : 3}


def one():
    score = 0
    for game in data:
        score += scores[game[1]]
        result = ( scores[game[1]] - scores[game[0]] + 1 ) % 3
        score += result*3
    return score

def two():
    score = 0
    for game in data:
        score += (scores[game[1]] - 1)*3
        score += ( scores[game[0]] + scores[game[1]]) % 3 + 1
    return score
    
print(two())


