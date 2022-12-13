lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace("\n","") for item in lines]

class Node:

    def __init__(self, coor, elevation):
        self.coor = coor
        self.elevation = elevation
        self.depth = 0

# Create nodes
graph = []
starting_point = None
end_point = None
for i in range(len(lines)):
    graph.append([])
    for j in range(len(lines[i])):
        graph[i].append(Node((i,j), ord(lines[i][j])-ord('a')))
        if lines[i][j] == "S":
            starting_point = graph[i][j]
            graph[i][j].elevation = 0
        elif lines[i][j] == "E":
            end_point = graph[i][j]
            graph[i][j].elevation = ord('z')-ord('a')

def handle_axis(coor, graph):
    tmp = []
    if coor[0] > 0:
        tmp.append((coor[0]-1,coor[1]))
    if coor[0] < len(graph)-1:
        tmp.append((coor[0]+1,coor[1]))
    if coor[1] > 0:
        tmp.append((coor[0],coor[1]-1))
    if coor[1] < len(graph[coor[0]])-1:
        tmp.append((coor[0],coor[1]+1))
    tmp = [graph[item[0]][item[1]] for item in tmp]
    return tmp


def link_tree(current_node, graph, node_to_find):
    queue = current_node.copy()
    visited = current_node

    while queue:
        current_node = queue.pop(0)
        if current_node == node_to_find:
            return current_node
        tmp = handle_axis(current_node.coor, graph)
        for i in range(len(tmp)):
            if tmp[i].elevation <= current_node.elevation+1:
                if tmp[i] not in visited and tmp[i] not in queue:
                    tmp[i].depth = current_node.depth+1
                    queue.append(tmp[i])
                    visited.append(tmp[i])

# link tree
current_node = starting_point
found_node = link_tree([current_node], graph, end_point)

print("Task 1: %s" %(found_node.depth))

starting_points = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        current_node = graph[i][j]
        if current_node.elevation == 0:
            starting_points.append(current_node)
            current_node.depth = 0

smallest = link_tree(starting_points, graph, end_point).depth

print("Task 2: %s" %(smallest))
