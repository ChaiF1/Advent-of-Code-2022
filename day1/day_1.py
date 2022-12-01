import numpy as np

file = open('day1_input.txt')


calories = np.array([], dtype=int)
cur_cal = 0

for line in file:
    if line == '\n':
        calories = np.append(calories, cur_cal)
        cur_cal = 0
    else:
        cur_cal += int(line)

calories = np.append(calories, cur_cal)
calories = np.sort(calories)
print(np.sum(calories[-3:]))
