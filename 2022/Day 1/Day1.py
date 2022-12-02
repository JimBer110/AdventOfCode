lines = []
with open("input.txt", 'r') as f:
    lines = f.readlines()

total_sum = 0
results = []
for i in range(len(lines)):

    if lines[i] == "\n":
        results.append(total_sum)
        total_sum = 0
    else:
        total_sum += int(lines[i])

print("Task 1: %s" %(max(results)))


total_sum = 0
for i in range(3):
    tmp = max(results)
    total_sum += tmp
    results.remove(tmp)

print("Task 2: %s" %(total_sum))
