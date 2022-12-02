lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

vowels = "aeiou"

banned = ['ab', 'cd', 'pq', 'xy']

total_count = 0
for i in range(len(lines)):
    vowel_count = 0
    double = False
    banned_word = False
    for j in range(len(lines[i])):
        if lines[i][j] in vowels:
            vowel_count += 1
        if j > 0 and lines[i][j-1] == lines[i][j]:
            double = True
        if j > 0 and lines[i][j-1:j+1] in banned:
            banned_word = True
    if vowel_count >= 3 and double and not banned_word:
        total_count += 1

print("Task 1: %s" %(total_count))

total_count = 0
for i in range(len(lines)):
    contains_pair = False
    double = False
    for j in range(2, len(lines[i])):
        tmp_pair = lines[i][j-2:j]
        if tmp_pair in lines[i][j:]:
            contains_pair = True
        if lines[i][j-2] == lines[i][j]:
            double = True
    if double and contains_pair:
        total_count += 1

print("Task 2: %s" %(total_count))
