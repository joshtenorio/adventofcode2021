data = open('input1.txt', 'r').read().split('\n')

# part 1
larger = 1 # hehehe
previous = data[0]
for i in range(1, len(data)):
    if previous < data[i]:
        larger += 1
    previous = data[i]
print(larger)

# part 2