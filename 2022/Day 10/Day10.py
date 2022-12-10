import sys
lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [item.replace("\n","") for item in lines]

def handle_crt(crt_pos, reg_x, text_str):
    if (crt_pos in range(reg_x-1,reg_x+2)):
        text_str += chr(0x2588)
    else:
        text_str += " "
    crt_pos = (crt_pos+1)%40
    if crt_pos == 0:
        text_str += "\n"
    return crt_pos, text_str

cycle = 1
reg_x = 1
crt_pos = 0
value_strengths = []
task2 = ""
for i in range(len(lines)):
    line = lines[i].split(" ")
    crt_pos, task2 = handle_crt(crt_pos, reg_x, task2)

    if line[0] == "noop":
        cycle+=1
    else:
        cycle+=1
        crt_pos, task2 = handle_crt(crt_pos, reg_x, task2)
        if (cycle+20) % 40 == 0:
            value_strengths.append(cycle*reg_x)
        cycle+=1
        reg_x+=int(line[1])

    if (cycle+20) % 40 == 0:
        value_strengths.append(cycle*reg_x)

print("Task 1: %s" %(sum(value_strengths)))
print("Task 2:")
print(task2)
