raw = open('input11', 'r').read().split('\n')
#raw = open('test', 'r').read().split('\n')

data = []
for row in raw:
    line = []
    for col in row:
        line.append(int(col))
    data.append(line)

def isFlashAvailable():
    for row in data:
        for col in row:
            if col >= 10:
                return True
    return False

def propagateFlash(i,j, fmap):
    global data
    data[i][j] = 0
    if i - 1 >= 0 and j - 1 >= 0:
        if not fmap[i-1][j-1]:
            data[i-1][j-1] += 1
    if j - 1 >= 0:
        if not fmap[i][j-1]:
            data[i][j-1] += 1
    if i - 1 >= 0:
        if not fmap[i-1][j]:
            data[i-1][j] += 1
    if i+1 < 10 and j+1 < 10:
        if not fmap[i+1][j+1]:
            data[i+1][j+1] += 1
    if i +1 < 10:
        if not fmap[i+1][j]:
            data[i+1][j] += 1
    if j+1 < 10:
        if not fmap[i][j+1]:
            data[i][j+1] += 1
    if i-1 >= 0 and j+1 < 10:
        if not fmap[i-1][j+1]:
            data[i-1][j+1] += 1
    if i+1 < 10 and j-1 >=0:
        if not fmap[i+1][j-1]:
            data[i+1][j-1] += 1
    
# part 1
numFlashes = 0
numSteps = 100
for n in range(numSteps):
    for i in range(10):
        for j in range(10):
            data[i][j] += 1
    
    flashMap = [ [False for i in range(10)]  for j in range(10)]
    while isFlashAvailable():
        for i in range(10):
            for j in range(10):
                if data[i][j] >= 10 and not flashMap[i][j]:
                    flashMap[i][j] = True
                    numFlashes+=1
                    propagateFlash(i,j, flashMap)


print(numFlashes)

print("---")

# part 2
numSteps = 3000
for n in range(numSteps):
    for i in range(10):
        for j in range(10):
            data[i][j] += 1
    
    flashMap = [ [False for i in range(10)]  for j in range(10)]
    while isFlashAvailable():
        for i in range(10):
            for j in range(10):
                if data[i][j] >= 10 and not flashMap[i][j]:
                    flashMap[i][j] = True
                    numFlashes+=1
                    propagateFlash(i,j, flashMap)
    numF = 0
    for row in flashMap:
        for col in row:
            if col:
                numF += 1
    if numF == 100:
        print(n+1)
        break
