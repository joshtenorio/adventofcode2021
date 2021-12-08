raw = open('input8.txt', 'r').read().split('\n')
#raw = open('test', 'r').read().split('\n')
#raw = open('test1', 'r').read().split('\n')

"""
0: 6 segments
1: 2 segments
2: 5 segments
3: 5 segments
4: 4 segments
5: 5 segments
6: 6 segments
7: 3 segments
8: 7 segments
9: 6 segments
"""

# part 1
count = 0
for display in raw:
    patterns = display.split(' | ')[0]
    output = display.split(' | ')[1].split(' ')

    for o in output:
        if len(o) == 2 or len(o) == 4 or len(o) == 3 or len(o) == 7:
            count += 1
    
print(count)
print("---")

# part 2
sum = 0
for display in raw:
    patterns = display.split(' | ')[0].split(' ')
    output = display.split(' | ')[1].split(' ')


    codes = ["","","","","","","","","",""]
    #       T - TL - BL - B - BR - TR - M
    segment = ["","","","","","",""]

    # first look for easy codes
    for p in patterns:
        if len(p) == 2:
            codes[1] = p
        elif len(p) == 4:
            codes[4] = p
        elif len(p) == 3:
            codes[7] = p
        elif len(p) == 7:
            codes[8] = p
    
    # codes[1] is a subset of codes[3]
    for p in patterns:
        if len(p) == 5:
            count = 0
            for c in p:
                if c in codes[1]:
                    count += 1
            if count == 2:
                codes[3] = p
                break
    
    # assign stuff to segments
    for c in codes[7]:
        if c not in codes[1]:
            segment[0] = c
            break
    for c in codes[4]:
        if c not in codes[3]:
            segment[1] = c
        elif c in codes[3] and c not in codes[1]:
            segment[6] = c
    
    # since we know TL, we know what codes[5] is
    # and can deduce codes[2]
    # can also find codes[0] since M is known
    for p in patterns:
        if len(p) == 5 and p != codes[3]:
            if segment[1] in p:
                codes[5] = p
            else:
                codes[2] = p
        elif len(p) == 6 and segment[6] not in p:
            codes[0] = p
    # assign BL and TR segments
    for c in codes[2]:
        if c not in codes[5] and c not in codes[1]:
            segment[2] = c
        elif c not in codes[5] and c in codes[1]:
            segment[5] = c
    # find codes[6] and codes[9]
    for p in patterns:
        if len(p) == 6 and p != codes[0]:
            if segment[2] not in p:
                codes[9] = p
            elif segment[2] in p:
                codes[6] = p

    lineNumber = ""
    for o in output:
        for i in range(len(codes)):
            if sorted(o) == sorted(codes[i]):
                lineNumber = lineNumber + str(i)

    sum += int(lineNumber)
print(sum)