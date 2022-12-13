lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace("\n","") for item in lines]

def do_compare(left, right):
    for a, b in zip(left, right):
        if type(a) == int and type(b) == int:
            if a < b:
                return 1
            elif a == b:
                continue
            else:
                return -1
        elif type(a) == int and type(b) == list:
            tmp = do_compare([a], b)
            if tmp == 0:
                continue
            else:
                return tmp
        elif type(a) == list and type(b) == int:
            tmp = do_compare(a, [b])
            if tmp == 0:
                continue
            else:
                return tmp
        else:
            tmp = do_compare(a, b)
            if tmp == 0:
                continue
            else:
                return tmp
    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    return 0

pairs = []
results = []
lines.append("")
all_elements = []
for i in range(len(lines)):
    if lines[i] == "":
        results.append(do_compare(pairs[0], pairs[1]))
        pairs = []
    else:
        pairs.append(eval(lines[i]))
        all_elements.append(eval(lines[i]))

total_sum = 0
for i in range(1, len(results)+1):
    if results[i-1] == 1:
        total_sum += i

print("Task 1: %s" %(total_sum))


key = [[2],[6]]

for i in range(1, len(all_elements)):
    j = i
    while j > 0 and do_compare(all_elements[j-1], all_elements[j]) == -1:
        tmp = all_elements[j-1]
        all_elements[j-1] = all_elements[j]
        all_elements[j] = tmp
        j -= 1

results = []
for i in range(len(key)):
    
    j = len(all_elements)
    all_elements.append(key[i])
    while j > 0 and do_compare(all_elements[j-1], all_elements[j]) == -1:
        tmp = all_elements[j-1]
        all_elements[j-1] = all_elements[j]
        all_elements[j] = tmp
        j -= 1
    results.append(j+1)

print("Task 2: %s" %(results[0]*results[1]))
