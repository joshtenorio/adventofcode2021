data = open('input3.txt', 'r').read().split('\n')
#data = open('test', 'r').read().split('\n')

# part 1
count0 = 0
count1 = 0
n = len(data[0]) # length of the binary string

g = ""
e = ""
for i in range(n):
    c0 = 0
    c1 = 0
    for row in data:
        char = row[i]
        if char == "0":
            c0 += 1
        else:
            c1 += 1

    if c0 > c1:
        g += "0"
        e += "1"
    else:
        g += "1"
        e += "0"

gamma = int(g,2)
epsilon = int(e,2)
        
print(gamma*epsilon)
print("----")

# part 2

# oxygen generator
dontconsider = []
while (len(data) - len(dontconsider)) > 1:
    for i in range(n):
        c0 = 0
        c1 = 0
        for row in data:
            if row in dontconsider:
                continue
            char = row[i]
            if char == "0":
                c0 += 1
            else:
                c1 += 1
    
        if c0 > c1:
            for row in data:
                char = row[i]
                if char == "1" and row not in dontconsider:
                    dontconsider.append(row)
        else:
            for row in data:
                char = row[i]
                if char == "0" and row not in dontconsider:
                    dontconsider.append(row)

o = ""
for row in data:
    if row not in dontconsider:
        o=row


# c02 scrubber
dontconsider = []
while (len(data) - len(dontconsider)) > 1:
    for i in range(n):
        c0 = 0
        c1 = 0
        for row in data:
            if row in dontconsider:
                continue
            char = row[i]
            if char == "0":
                c0 += 1
            else:
                c1 += 1
    
        if c0 <= c1:
            for row in data:
                char = row[i]
                if char == "1" and row not in dontconsider:
                    dontconsider.append(row)
        else:
            for row in data:
                char = row[i]
                if char == "0" and row not in dontconsider:
                    dontconsider.append(row)
        if (len(data) - len(dontconsider)) <= 1:
            break

c = ""
for row in data:
    if row not in dontconsider:
        c = row


ox = int(o,2)
co = int(c,2)
        
print(ox*co)