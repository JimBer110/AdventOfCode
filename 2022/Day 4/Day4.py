lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

def removeElements(A, B):
    n = len(A)
    return any(A == B[i:i + n] for i in range(len(B)-n + 1))


total_com_over = 0
total_par_over = 0
for i in range(len(lines)):
    line = lines[i].split(",")

    line[0] = list(range(int(line[0].split("-")[0]), int(line[0].split("-")[1])+1))
    line[1] = list(range(int(line[1].split("-")[0]), int(line[1].split("-")[1])+1))

    if removeElements(line[0], line[1]) or removeElements(line[1], line[0]):
        total_com_over += 1

    for j in range(len(line[0])):
        if line[0][j] in line[1]:
            total_par_over += 1
            break

print("Task 1: %s" %(total_com_over))
print("Task 2: %s" %(total_par_over))
