lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace('\n','') for item in lines]

def get_distance(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def is_within(point, interval):
    return point >= interval[0] and point <= interval[1]

def handle_overlap(range1, range2, clamp=False):
    if clamp:
        if range1[0] < 0:
            range1 = (0, range1[1])
        if range1[1] > 4000000:
            range1 = (range1[0], 4000000)
        if range2[0] < 0:
            range2 = (0, range2[1])
        if range2[1] > 4000000:
            range2 = (range2[0], 4000000)

    if range2[1] < range2[0]:
        return range1, range2, False

    if range1[0] <= range2[0] and is_within(range1[1], range2):
        return (range1[0], range2[1]), (0,-1), True
    elif is_within(range1[0], range2) and range1[1] >= range2[1]:
        return (range2[0], range1[1]), (0,-1), True
    elif is_within(range1[0], range2) and is_within(range1[1], range2):
        return (range2[0], range2[1]), (0,-1), True
    elif is_within(range2[0], range1) and is_within(range2[1], range1):
        return (range1[0], range1[1]), (0,-1), True
    else:
        return range1, range2, False

sensors = []
for line in lines:
    tmp = {}
    tmp['coor'] = (int(line.split(' ')[2].split("=")[1][:-1]),
                   int(line.split(' ')[3].split("=")[1][:-1]))
    tmp['beacon'] =(int(line.split(' ')[8].split("=")[1][:-1]),
                   int(line.split(' ')[9].split("=")[1]))
    tmp['distance'] = get_distance(tmp['coor'], tmp['beacon'])
    sensors.append(tmp)

ranges = []
for sensor in sensors:
    point = [sensor['coor'][0], 2000000]
    tmp_distance = sensor['distance'] - get_distance(sensor['coor'], point) 
    if tmp_distance >= 0:
        ranges.append((point[0]-tmp_distance, point[0]+tmp_distance))

did_change = True
while did_change:
    did_change = False
    for i in range(len(ranges)-1):
        for j in range(i+1, len(ranges)):
            ranges[i], ranges[j], tmp = handle_overlap(ranges[i], ranges[j])
            if not did_change:
                did_change = tmp
ranges = [item for item in ranges if item != (0, -1)]

total_sum = 0
for i in range(len(ranges)):
    total_sum += ranges[i][1]-ranges[i][0]

print("Task 1: %s" %(total_sum))


ranges = []
max_size = 4000000
for i in range(max_size):
    print("%s/%s" %(i+1, max_size), end="\r")
    ranges.append([])
    for sensor in sensors:
        point = [sensor['coor'][0], i]
        tmp_distance = sensor['distance'] - get_distance(sensor['coor'], point) 
        if tmp_distance >= 0:
            ranges[i].append((point[0]-tmp_distance, point[0]+tmp_distance))
print()

for k in range(len(ranges)):
    print("%s/%s" %(k+1, max_size), end="\r")
    did_change = True
    while did_change:
        did_change = False
        for i in range(len(ranges[k])-1):
            for j in range(i+1, len(ranges[k])):
                ranges[k][i], ranges[k][j], tmp = handle_overlap(ranges[k][i], ranges[k][j], True)
                if not did_change:
                    did_change = tmp
    ranges[k] = [item for item in ranges[k] if item != (0, -1)]
print()

x_val = 0
y_val = 0
for i in range(len(ranges)):
    if len(ranges[i]) > 1:
        y_val = i
        x_val = min(ranges[i][0][1], ranges[i][1][1])+1

print("Task 2: %s" %(x_val*max_size+y_val))
