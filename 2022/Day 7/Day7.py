lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace("\n", "") for item in lines]

def add_to_tree(item, current_dir):
    tmp_data = data
    for i in range(len(current_dir)):
        tmp_data = tmp_data[current_dir[i]]
    if item[0] == "dir":
        tmp_data[item[1]] = {}
    else:
        tmp_data[item[1]] = int(item[0])

def traverse_tree(current_dir):
    dir_sizes = []
    tmp_data = data
    for i in range(len(current_dir)):
        tmp_data = tmp_data[current_dir[i]]
    dict_sum = 0
    for i in tmp_data.keys():
        if (type(tmp_data[i]) == dict):
            dir_sizes += traverse_tree(current_dir+[i])
            dict_sum += dir_sizes[-1][1]
        else:
            dict_sum += tmp_data[i]
    tmp = ("/".join(current_dir)[1:], dict_sum)
    dir_sizes.append(tmp)
    return dir_sizes

current_dir = []
data = {'/': {}}
for i in range(len(lines)):
    line = lines[i].split(" ")

    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                current_dir = ["/"]
            elif line[2] == "..":
                current_dir.pop()
            else:
                current_dir.append(line[2])
    else:
        add_to_tree(line, current_dir)

all_dir_sizes = traverse_tree(["/"])
total_sum = 0
for i in range(len(all_dir_sizes)):
    if all_dir_sizes[i][1] <= 100000:
        total_sum += all_dir_sizes[i][1]

print("Task 1: %s" %(total_sum))


needed_space = 30000000 - 70000000 + all_dir_sizes[-1][1]
current_smallest = all_dir_sizes[-1][1]
for i in range(len(all_dir_sizes)):
    if all_dir_sizes[i][1] >= needed_space:
        if all_dir_sizes[i][1]  < current_smallest:
            current_smallest = all_dir_sizes[i][1]

print("Task 2: %s" %(current_smallest))
