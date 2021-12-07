raw = open('input7.txt', 'r').read().split(',')
#raw = open('test', 'r').read().split(',')

print("input size: " + str(len(raw)))
data = []
for r in raw:
    data.append(int(r))
# part 1
min = -1
pos = 0
for pos in data:
    align = pos
    fuel = 0
    for pos in data:
        fuel += abs(pos-align)
    if min == -1:
        min = fuel
        pos = align
    elif fuel < min:
        min = fuel
        pos = align

print(pos)
print(min)
print("---")

# part 2

def getFuelCost(start, target):
    numSteps = abs(target-start)
    sum = 0
    for i in range(numSteps+1):
        sum += i
    return sum

min = -1
pos = 0

dMin = 123123131
dMax = -1
for pos in data:
    if pos > dMax:
        dMax = pos
    elif pos < dMin:
        dMin = pos
for pos in range(dMin, int((dMax+1)/2)):
    align = pos
    fuel = 0
    for pos in data:
        fuel += getFuelCost(pos, align)
    #print("align: " + str(align) + "; fuel cost: " + str(fuel))
    if min == -1:
        min = fuel
        pos = align
    elif fuel < min:
        min = fuel
        pos = align

print(pos)
print(min)
print("---")