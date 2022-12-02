line = ""
with open('input.txt', 'r') as f:
    line = f.read()

current_pos = (0,0)
all_coordinates = [current_pos]

santa_current_pos = (0,0)
roboot_santa_current_pos = (0,0)
all_all_coordinates = [(0,0)]
for i in range(len(line)):
    if (line[i] == '^'):
        current_pos = (current_pos[0], current_pos[1]-1)
    elif (line[i] == 'v'):
        current_pos = (current_pos[0], current_pos[1]+1)
    elif (line[i] == '>'):
        current_pos = (current_pos[0]+1, current_pos[1])
    elif (line[i] == '<'):
        current_pos = (current_pos[0]-1, current_pos[1])
    
    if current_pos not in all_coordinates:
        all_coordinates.append(current_pos)

    active_pos = None
    if i % 2 == 0:
        active_pos = santa_current_pos
    else:
        active_pos = roboot_santa_current_pos

    if (line[i] == '^'):
        active_pos = (active_pos[0], active_pos[1]-1)
    elif (line[i] == 'v'):
        active_pos = (active_pos[0], active_pos[1]+1)
    elif (line[i] == '>'):
        active_pos = (active_pos[0]+1, active_pos[1])
    elif (line[i] == '<'):
        active_pos = (active_pos[0]-1, active_pos[1])

    if active_pos not in all_all_coordinates:
        all_all_coordinates.append(active_pos)

    if i % 2 == 0:
        santa_current_pos = active_pos
    else:
        roboot_santa_current_pos = active_pos

print("Task 1: %s" %len(all_coordinates))
print("Task 2: %s" %len(all_all_coordinates))
