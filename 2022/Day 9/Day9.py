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
        if (head[0] > tail[0] and head[1] > tail[1]):
            return (tail[0]+1, tail[1]+1)
        if (head[0] > tail[0] and head[1] < tail[1]):
            return (tail[0]+1, tail[1]-1)
        if (head[0] < tail[0] and head[1] > tail[1]):
            return (tail[0]-1, tail[1]+1)
        if (head[0] < tail[0] and head[1] < tail[1]):
            return (tail[0]-1, tail[1]-1)


def handle_movement(rope, tail_visited, line):
    for i in range(int(line[1])):
        if line[0] == "U":
            rope[0] = (rope[0][0], rope[0][1]-1)
        elif line[0] == "D":
            rope[0] = (rope[0][0], rope[0][1]+1)
        elif line[0] == "L":
            rope[0] = (rope[0][0]-1, rope[0][1])
        else:
            rope[0] = (rope[0][0]+1, rope[0][1])

        if rope[0] not in tail_visited[0]:
            tail_visited[0].append(rope[0])

        for j in range(1, len(rope)):
            if get_distance(rope[j-1], rope[j]) > 1:
                rope[j] = handle_follow(rope[j], rope[j-1])
                if rope[j] not in tail_visited[j]:
                    tail_visited[j].append(rope[j])

starting_pos = (0,0)
rope_len = 10
tail_visited = [[starting_pos] for i in range((rope_len))]
rope = [starting_pos]*rope_len

for i in range(len(lines)):
    handle_movement(rope, tail_visited, lines[i].split(" "))

print("Task 1: %s" %(len(tail_visited[1])))
print("Task 2: %s" %(len(tail_visited[9])))
