from collections import defaultdict, Counter

raw = open('input12', 'r').read().split('\n')
#raw = open('test', 'r').read().split('\n')

# part 1
numPaths = 0
def BFS(paths, path):
    global numPaths
    pos = path[-1]
    if(pos == 'end'):
        numPaths+=1
        return
    for n in paths[pos]:
        if n.islower() and n in path:
            continue
        BFS(paths, path+[n])

adjList = defaultdict(list)
for edge in raw:
    start, end = edge.split('-')
    adjList[start].append(end)
    adjList[end].append(start)

BFS(adjList, ["start"])
print(numPaths)


print("---")

# part 2
numPaths = 0
def canRevisit(path):
    smallCaves = []
    for p in path:
        if p.islower():
            smallCaves.append(p)
    counts = Counter(smallCaves)
    for c in counts.values():
        if c > 1:
            return False
    return True

def BFS2(paths, path):
    global numPaths
    pos = path[-1]
    if(pos == 'end'):
        numPaths+=1
        return
    for n in paths[pos]:
        if n == "start":
            continue
        if not n.islower() or n not in path or canRevisit(path):
            BFS2(paths, path+[n])

BFS2(adjList, ["start"])
print(numPaths)