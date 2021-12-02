data = open('input2.txt', 'r').read().split('\n')
#data = open('test', 'r').read().split('\n')

# part 1
horizontal = 0
depth = 0

for op in data:
    line = op.split(" ")
    if line[0] == "forward":
        horizontal += int(line[1])
    elif line[0] == "down":
        depth += int(line[1])
    elif line[0] == "up":
        depth -= int(line[1])

print(horizontal)
print(depth)
print(horizontal*depth)

print("---")
# part 2
horizontal = 0
depth = 0
aim = 0
for op in data:
    line = op.split(" ")
    if line[0] == "forward":
        horizontal += int(line[1])
        depth += int(line[1])*aim
    elif line[0] == "down":
        aim += int(line[1])
    elif line[0] == "up":
        aim -= int(line[1])

print(horizontal)
print(depth)
print(horizontal*depth)