import numpy as np


file = open('day_4_data.txt')
data = np.empty((0,4), dtype=int)

for line in file:
    ranges = line.strip('\n').replace('-', ',').split(',')
    ranges = list(map(int, ranges))
    data = np.append(data, [ranges], axis=0)

def one():
    answer = 0
    for pair in data:
        if pair[0] <= pair[2] and pair[1] >= pair[3]:
            answer += 1
        elif pair[0] >= pair[2] and pair[1] <= pair[3]:
            answer += 1
    return answer

def two():
    no_lap = 0
    for pair in data:
        if pair[1] < pair[2] or pair[0] > pair[3]:
            no_lap += 1
    return len(data)-no_lap
    
print(two())
            

