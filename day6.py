data = open('input6.txt', 'r').read().split(',')
#data = open('test', 'r').read().split(',')


fishes = []
for d in data:
    fishes.append(int(d))

nDays = 80 # part 1: d=80 ; part 2: d=256
for i in range(nDays):
    for j in range(len(fishes)):
        if fishes[j] == 0:
            fishes[j] = 6
            fishes.append(8)
            continue
        fishes[j] -= 1
    

    print("day " + str(i))


print(len(fishes))