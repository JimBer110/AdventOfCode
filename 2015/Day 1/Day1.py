line = ""
with open('input.txt', 'r') as f:
    line = f.read()


floor = 0
base_index = 0
for i in range(len(line)):
    if line[i] == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1 and base_index == 0:
        base_index = i+1

print("Task 1: %s" %(floor))
print("Task 2: %s" %(base_index))
