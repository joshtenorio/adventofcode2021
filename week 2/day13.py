from collections import defaultdict, Counter

raw = open('input13', 'r').read().split('\n\n')
#raw = open('test', 'r').read().split('\n\n')

rawdots = raw[0].split('\n')
instructions = raw[1].split('\n')

# part 1
dots = set(rawdots)

line = instructions[0].split(" ")[2].split("=")
for d in dots.copy():
    c = d.split(",")
    x = int(c[0])
    y = int(c[1])
    if line[0] == 'y':
        if y <= int(line[1]): # no need to adjust
            continue
        
        y = int(line[1]) - y + int(line[1])
    else:
        if x <= int(line[1]): # no need to adjust
            continue
    
        x = int(line[1]) - x + int(line[1])

    dots.remove(d)
    dots.add(str(x) + "," + str(y))

print(len(dots))
print("---")

# part 2

dots = set(rawdots)
for i in instructions:
    line = i.split(" ")[2].split("=")
    for d in dots.copy():
        c = d.split(",")
        x = int(c[0])
        y = int(c[1])
        if line[0] == 'y':
            if y <= int(line[1]): # no need to adjust
                continue
            
            y = int(line[1]) - y + int(line[1])
        else:
            if x <= int(line[1]): # no need to adjust
                continue
        
            x = int(line[1]) - x + int(line[1])

        dots.remove(d)
        dots.add(str(x) + "," + str(y))


xmax = -1
ymax = -1
for d in dots:
    c = d.split(",")
    x = int(c[0])
    y = int(c[1])
    if x > xmax:
        xmax = x
    if y > ymax:
        ymax = y
paper = [ ["." for i in range(xmax+1)] for j in range(ymax+1)]
for d in dots:
    c = d.split(",")
    x = int(c[0])
    y = int(c[1])
    paper[y][x] = "#"

sum = 0
for row in paper:
    print(row)
    for col in row:
        if col == "#":
            sum += 1
print(sum)