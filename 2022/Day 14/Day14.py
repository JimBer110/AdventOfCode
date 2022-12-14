lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace('\n','') for item in lines]

def print_board(board):
    for i in range(len(board)):
        print("".join(board[i]))

def draw_lines(board, first_pos, second_pos):
    min_x = min(first_pos[0], second_pos[0])
    max_x = max(first_pos[0], second_pos[0])
    min_y = min(first_pos[1], second_pos[1])
    max_y = max(first_pos[1], second_pos[1])
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            board[j][i] = "#"

class Sand:

    def __init__(self, board, pos):
        self.pos = pos
        self.board = board
    
    def update(self):
        falling = True
        while falling:
            if self.pos[1] >= len(self.board)-1:
                self.pos[1] += 1
                falling = False
            elif self.board[self.pos[1]+1][self.pos[0]] == ".":
                self.pos[1] = self.pos[1]+1
            elif self.board[self.pos[1]+1][self.pos[0]-1] == ".":
                self.pos[0] = self.pos[0]-1
                self.pos[1] = self.pos[1]+1
            elif self.board[self.pos[1]+1][self.pos[0]+1] == ".":
                self.pos[0] = self.pos[0]+1
                self.pos[1] = self.pos[1]+1
            else:
                falling = False
        return self.pos

for i in range(len(lines)):
    lines[i] = lines[i].split(" -> ")
    for j in range(len(lines[i])):
        lines[i][j] = (int(lines[i][j].split(",")[0]),int(lines[i][j].split(",")[1]))
x_range = [lines[0][0][0],lines[0][0][0]]
y_range = [0,lines[0][0][1]]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if x_range[0] > lines[i][j][0]:
            x_range[0] = lines[i][j][0]
        if x_range[1] < lines[i][j][0]:
            x_range[1] = lines[i][j][0]
        if y_range[0] > lines[i][j][1]:
            y_range[0] = lines[i][j][1]
        if y_range[1] < lines[i][j][1]:
            y_range[1] = lines[i][j][1]

board = []
for i in range(y_range[0],y_range[1]+1):
    board.append(['.']*(x_range[1]-x_range[0]+1))

for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = (lines[i][j][0]-x_range[0],lines[i][j][1])

for i in range(len(lines)):
    for j in range(1, len(lines[i])):
        draw_lines(board, lines[i][j-1], lines[i][j])

result_counter = 0
while True:
    tmp_sand = Sand(board, [500-x_range[0], 0])
    tmp = tmp_sand.update()
    if tmp[1] == len(board):
        break
    result_counter += 1
    board[tmp[1]][tmp[0]] = "o"

print("Task 1: %s" %(result_counter))


for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = (lines[i][j][0]+x_range[0],lines[i][j][1])

board = []
tmp_mid = 500
tmp_range = 170
x_range = (tmp_mid-tmp_range,tmp_mid+tmp_range)
for i in range(y_range[0],y_range[1]+2):
    board.append(['.']*(x_range[1]-x_range[0]+1))

for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = (lines[i][j][0]-x_range[0],lines[i][j][1])

for i in range(len(lines)):
    for j in range(1, len(lines[i])):
        draw_lines(board, lines[i][j-1], lines[i][j])

result_counter = 0
while True:
    tmp_sand = Sand(board, [500-x_range[0], 0])
    tmp = tmp_sand.update()
    result_counter += 1
    if tmp[1] == len(board):
        tmp[1] -= 1
    if tmp[0] < 0:
        raise "Out of bounds"
    board[tmp[1]][tmp[0]] = "o"
    if tmp == [500-x_range[0], 0]:
        break

print("Task 2: %s" %(result_counter))

