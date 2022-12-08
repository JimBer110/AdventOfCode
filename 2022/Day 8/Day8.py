grid = []
with open('input.txt', 'r') as f:
    grid = f.readlines()

grid = [list(item.replace("\n","")) for item in grid]

def is_visible(coor, grid):
    _visible = True
    for i in range(coor[0]):
        if grid[i][coor[1]] >= grid[coor[0]][coor[1]]:
            _visible = False
            break
    _hidden = not _visible
    if _hidden:
        _visible = True
        for i in range(coor[0]+1, len(grid)):
            if grid[i][coor[1]] >= grid[coor[0]][coor[1]]:
                _visible = False
                break
        _hidden = not _visible
    if _hidden:
        _visible = True
        for i in range(coor[1]):
            if grid[coor[0]][i] >= grid[coor[0]][coor[1]]:
                _visible = False
                break
        _hidden = not _visible
    if _hidden:
        _visible = True
        for i in range(coor[1]+1, len(grid[coor[0]])):
            if grid[coor[0]][i] >= grid[coor[0]][coor[1]]:
                _visible = False
                break
        _hidden = not _visible
    return not _hidden

def scenic_score(coor, grid):
    view = []
    view_sum = 0
    for i in range(coor[0]-1, -1, -1):
        view_sum += 1
        if grid[i][coor[1]] >= grid[coor[0]][coor[1]]:
            break
    view.append(view_sum)

    view_sum = 0
    for i in range(coor[0]+1, len(grid)):
        view_sum += 1
        if grid[i][coor[1]] >= grid[coor[0]][coor[1]]:
            _visible = False
            break
    view.append(view_sum)

    view_sum = 0
    for i in range(coor[1]-1, -1, -1):
        view_sum += 1
        if grid[coor[0]][i] >= grid[coor[0]][coor[1]]:
            _visible = False
            break
    view.append(view_sum)

    view_sum = 0
    for i in range(coor[1]+1, len(grid[coor[0]])):
        view_sum += 1
        if grid[coor[0]][i] >= grid[coor[0]][coor[1]]:
            _visible = False
            break
    view.append(view_sum)

    total_score = 1
    for i in range(len(view)):
        total_score *= view[i]
    return total_score


visible = len(grid)*2+(len(grid[0])-2)*2
best_scenic_score = 0

for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):
        if is_visible((i,j), grid):
            visible += 1
        tmp = scenic_score((i,j),grid)
        if tmp > best_scenic_score:
            best_scenic_score = tmp

print("Task 1: %s" %(visible))
print("Task 2: %s" %(best_scenic_score))
