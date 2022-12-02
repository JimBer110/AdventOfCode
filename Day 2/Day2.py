lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

total_score = 0
for i in range(len(lines)):

    if lines[i][2] == 'X':
        total_score += 1
    elif lines[i][2] == 'Y':
        total_score += 2
    else: 
        total_score += 3

    if ord(lines[i][0])-ord('A') == ord(lines[i][2])-ord('X'):
        total_score += 3
    elif lines[i][0] == 'A' and lines[i][2] == 'Y':
        total_score += 6
    elif lines[i][0] == 'B' and lines[i][2] == 'Z':
        total_score += 6
    elif lines[i][0] == 'C' and lines[i][2] == 'X':
        total_score += 6

print("Task 1: %s" %(total_score))


total_score = 0
for i in range(len(lines)):

    if lines[i][2] == 'X':
        if lines[i][0] == 'A':
            total_score += 3
        elif lines[i][0] == 'B':
            total_score += 1
        else:
            total_score += 2
    elif lines[i][2] == 'Y':
        total_score += 3
        total_score += ord(lines[i][0])-64
    else: 
        total_score += 6
        if lines[i][0] == 'A':
            total_score += 2
        elif lines[i][0] == 'B':
            total_score += 3
        else:
            total_score += 1

print("Task 2: %s" %(total_score))

