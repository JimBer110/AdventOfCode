stream = ""
with open('input.txt', 'r') as f:
    stream = f.read()

packet_start = 0
message_start = 0
for i in range(3, len(stream)):

    failed = False
    for j in range(3, 0, -1):
        if (stream[i-j] in stream[i-j+1:i+1]):
            failed = True
            break
    
    if not failed and packet_start == 0:
        packet_start = i+1

    failed = False
    for j in range(13, 0, -1):
        if i < 13:
            failed = True
            break
        if (stream[i-j] in stream[i-j+1:i+1]):
            failed = True
            break

    if not failed:
        message_start = i+1


print("Task 1: %s" %(packet_start))
print("Task 2: %s" %(message_start))
