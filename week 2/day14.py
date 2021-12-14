from collections import defaultdict, Counter

raw = open('input14', 'r').read().split('\n\n')
#raw = open('test', 'r').read().split('\n\n')

template = raw[0]
rulesRaw = raw[1].split('\n')

# part 1
numSteps = 10
output = template[0]
for i in range(len(template)-1):
    window = template[i:i+2]
    for rule in rulesRaw:
        pair = rule.split(" -> ")[0]
        insert = rule.split(" -> ")[1]
        if window == pair:
            output += insert
    output += window[1]

for i in range(numSteps-1):
    template = output
    output = template[0]

    for i in range(len(template)-1):
        window = template[i:i+2]

        for rule in rulesRaw:
            pair = rule.split(" -> ")[0]
            insert = rule.split(" -> ")[1]
            if window == pair:

                output += insert
        output += window[1]

counter = Counter(output).most_common(26)
print(counter)
print(counter[0][1] - counter[-1][1])


print("---")

# part 2
rules = {
    rule.split(" -> ")[0] : rule.split(" -> ")[1] for rule in rulesRaw
}
numSteps = 40

# reset template lol
template = raw[0]

paircounter = Counter()
for i in range(len(template)-1):
    paircounter[template[i:i+2]] += 1

for i in range(numSteps):
    newPairs = Counter()
    for pair, value in paircounter.items():
        first = pair[0]
        second = pair[1]
        mid = rules[pair]
        newPairs[first+mid] += value
        newPairs[mid+second] += value
    paircounter = newPairs

charcounter = Counter()
charcounter[template[-1]] += 1
for pair, value in paircounter.items():
    charcounter[pair[0]] += value

print(charcounter.most_common()[0][1] - charcounter.most_common()[-1][1])