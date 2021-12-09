data = open('input1.txt', 'r').read().split('\n')

# part 1
larger = 0
previous = int(data[0])
for i in range(1, len(data)):
    if previous < int(data[i]):
        larger += 1
    previous = int(data[i])
print(larger)

# part 2
larger = 0
previousWindow = int(data[0]) + int(data[1]) + int(data[2])
for i in range(1, len(data)-2):
    currWindow = int(data[i]) + int(data[i+1]) + int(data[i+2])
    if currWindow > previousWindow:
        larger += 1
    previousWindow = currWindow
print(larger)
