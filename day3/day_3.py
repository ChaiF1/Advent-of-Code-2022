import numpy as np

data = np.loadtxt('day_3_data.txt', dtype = str)
answer = 0

def one():
    answer = 0
    for rucksack in data:
        items = len(rucksack)//2
        item = list(set(rucksack[:items]) & set(rucksack[items:]))[0]
        if item == item.capitalize():
            answer += ord(item) - 64 + 26
        else:
            answer += ord(item) - 96
    return answer

def two():
    answer = 0
    for k in range(len(data)//3):
        badge = list(set(data[3*k]) & set(data[3*k+1]) & set(data[3*k+2]))[0]
        if badge == badge.capitalize():
            answer += ord(badge) - 64 + 26
        else:
            answer += ord(badge) - 96
    return answer
print(two())

