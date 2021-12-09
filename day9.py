raw = open('input9.txt', 'r').read().split('\n')
raw = open('test', 'r').read().split('\n')

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
        current = data[i][j]
        north = 99
        south = 99
        west = 99
        east = 99

        if i-1 >= 0:
            north = data[i-1][j]
        if i+1 < yMax:
            south = data[i+1][j]
        if j-1 >= 0:
            west = data[i][j-1]
        if j+1 < xMax:
            east = data[i][j+1]
        
        if(
            current < north and
            current < east and
            current < south and
            current < west
        ):
            sumRisk += 1 + current
print(sumRisk)
print("---")

# part 2
sumRisk = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        current = data[i][j]
        if current == 9:
            continue
        north = 99
        south = 99
        west = 99
        east = 99

        if i-1 >= 0:
            north = data[i-1][j]
        if i+1 < yMax:
            south = data[i+1][j]
        if j-1 >= 0:
            west = data[i][j-1]
        if j+1 < xMax:
            east = data[i][j+1]
        
        if(
            current < north and
            current < east and
            current < south and
            current < west
        ):
            sumRisk += 1 + current
print(sumRisk)