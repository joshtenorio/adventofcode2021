raw = open('input9.txt', 'r').read().split('\n')
#raw = open('test', 'r').read().split('\n')

def isLocalMin(j, i, map):
    current = map[i][j]
    north = 99
    south = 99
    west = 99
    east = 99

    if i-1 >= 0:
        north = map[i-1][j]
    if i+1 < yMax:
        south = map[i+1][j]
    if j-1 >= 0:
        west = map[i][j-1]
    if j+1 < xMax:
        east = map[i][j+1]
    
    if(
        current < north and
        current < east and
        current < south and
        current < west
    ):
        return [True, current]
    return [False, 0]

data = []
for row in raw:
    r = []
    for j in row:
        r.append(int(j))
    data.append(r)

min = 0
xMax = len(data[0])
yMax = len(data)

# part 1
sumRisk = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        output = isLocalMin(j, i, data)
        if output[0]:
            sumRisk += 1 + output[1]
print(sumRisk)
print("---")

# part 2
def inside(x, y):
    if y < 0 or x < 0 or x >= xMax or y >= yMax:
        return False
    if data[y][x] == 9:
        return False
    return True


v = []
def getBasinSize(x,y):
    if not inside(x,y):
        return 0
    q = []
    q.append([x,y])

    size = 0
    while len(q) != 0:
        n = q.pop(0)
        if inside(n[0], n[1]) and n not in v:
            size += 1
            q.append([n[0] - 1, n[1]])
            q.append([n[0] + 1, n[1]])
            q.append([n[0], n[1] - 1])
            q.append([n[0], n[1] + 1])
            v.append(n)
    return size

basins = []
for i in range(len(data)):
    for j in range(len(data[0])):
        basins.append(getBasinSize(j,i))

basins.sort(reverse = True)
print(basins[0] * basins[1] * basins[2])
