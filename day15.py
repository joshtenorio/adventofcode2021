from abc import abstractproperty
from collections import defaultdict, Counter
import heapq
raw = open('input15', 'r').read().split('\n')
raw = open('test', 'r').read().split('\n')


data = [ [int(raw[j][i]) for i in range(len(raw[0]))] for j in range(len(raw))]



def getNeighbors(x,y):
    neighbors = []
    if x > 0:
        neighbors.append((x-1,y))
    if y > 0:
        neighbors.append((x,y-1))
    if x < len(data[0])-1:
        neighbors.append((x+1,y))
    if y < len(data)-1:
        neighbors.append((x,y+1))
    return neighbors

# part 1
risk = 0




print("---")

# part 2

