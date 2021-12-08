raw = open('input8.txt', 'r').read().split('\n')
raw = open('test', 'r').read().split('\n')

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
    
    # assign stuff to segments
    for c in codes[7]:
        if c not in codes[1]:
            segment[0] = c
            break
    

    lineNumber = ""
    for o in output:
        if len(o) == 2 or len(o) == 4 or len(o) == 3 or len(o) == 7:
            pass
    sum += int(lineNumber)
print(sum)