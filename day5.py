data = open('input5.txt', 'r').read().split('\n')
#data = open('test', 'r').read().split('\n')


xSize = 0
ySize = 0
# first look for xmax and ymax so we know how big bitboard to make

for line in data:
    points = line.split(" -> ")
    for p in points:
        coords = p.split(",")
        if int(coords[0]) > xSize:
            xSize = int(coords[0])
        if int(coords[1]) > ySize:
            ySize = int(coords[1])

print("xmax: " + str(xSize))
print("ymax: " + str(ySize))

# part 1
bitboard = [[0 for x in range(ySize+1)] for y in range(xSize+1)]

for line in data:
    first = line.split(" -> ")[0].split(',')
    second = line.split(" -> ")[1].split(',')
    # figure out if its horizontal or vertical

    # vertical
    if int(first[0]) == int(second[0]):
        if(int(first[1]) < int(second[1])):
            for y in range(int(first[1]), int(second[1])+1):
                bitboard[int(first[0])][y] += 1
        else:
            for y in range(int(second[1]), int(first[1])+1):
                bitboard[int(first[0])][y] += 1
    # horizontal
    elif int(first[1]) == int(second[1]):
        if(int(first[0]) < int(second[0])):
            for x in range(int(first[0]), int(second[0])+1):
                bitboard[x][int(first[1])] += 1
        else:
            for x in range(int(second[0]), int(first[0])+1):
                bitboard[x][int(first[1])] += 1


count = 0
for row in bitboard:
    for c in row:
        if c >= 2:
            count += 1
print(count)
print("----")

# part 2
bitboard = [[0 for x in range(ySize+1)] for y in range(xSize+1)]

for line in data:
    first = line.split(" -> ")[0].split(',')
    second = line.split(" -> ")[1].split(',')

    # vertical
    if int(first[0]) == int(second[0]):
        if(int(first[1]) < int(second[1])):
            for y in range(int(first[1]), int(second[1])+1):
                bitboard[int(first[0])][y] += 1
        else:
            for y in range(int(second[1]), int(first[1])+1):
                bitboard[int(first[0])][y] += 1
    # horizontal
    elif int(first[1]) == int(second[1]):
        if(int(first[0]) < int(second[0])):
            for x in range(int(first[0]), int(second[0])+1):
                bitboard[x][int(first[1])] += 1
        else:
            for x in range(int(second[0]), int(first[0])+1):
                bitboard[x][int(first[1])] += 1
    # diagonal
    else:
        firstX = int(first[0])
        firstY = int(first[1])
        secondX = int(second[0])
        secondY = int(second[1])
        deltaX = secondX - firstX
        deltaY = secondY - firstY
        x = firstX
        y = firstY
        while (x != secondX+ deltaX/abs(deltaX)) and (y != secondY+deltaY/abs(deltaY)):
            bitboard[x][y] += 1
            if deltaX > 0:
                x += 1
            else:
                x -=1
            if deltaY > 0:
                y += 1
            else:
                y -= 1



count = 0
for row in bitboard:
    #print(row)
    for c in row:
        if c >= 2:
            count += 1
print(count)