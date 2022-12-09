lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace("\n","") for item in lines]


def get_distance(coor1, coor2):
    return max(abs(coor1[0]-coor2[0]), abs(coor1[1]-coor2[1]))

def handle_follow(tail, head):
    if tail[0] == head[0] or tail[1] == head[1]:
        if tail[0] == head[0]:
            if tail[1] < head[1]:
                return (tail[0], tail[1]+1)
            else:
                return (tail[0], tail[1]-1)
        else:
            if tail[0] < head[0]:
                return (tail[0]+1, tail[1])
            else:
                return (tail[0]-1, tail[1])
    else:
        if abs(tail[0]-head[0]) == 1:
            return handle_follow((head[0], tail[1]), head)
        else:
            return handle_follow((tail[0], head[1]), head)

def handle_movement(head_pos, tail_pos, tail_visited, line):
    for i in range(int(line[1])):
        if line[0] == "U":
            head_pos = (head_pos[0], head_pos[1]-1)
        elif line[0] == "D":
            head_pos = (head_pos[0], head_pos[1]+1)
        elif line[0] == "L":
            head_pos = (head_pos[0]-1, head_pos[1])
        else:
            head_pos = (head_pos[0]+1, head_pos[1])
        if get_distance(head_pos, tail_pos) > 1:
            tail_pos = handle_follow(tail_pos, head_pos)
            if tail_pos not in tail_visited:
                tail_visited.append(tail_pos)
    return head_pos, tail_pos, tail_visited

starting_pos = (0,0)
tail_pos = starting_pos
head_pos = starting_pos
tail_visited = [starting_pos]

for i in range(len(lines)):
    head_pos, tail_pos, tail_visited = handle_movement(head_pos, tail_pos, tail_visited, lines[i].split(" "))

print("Task 1: %s" %(len(tail_visited)))
