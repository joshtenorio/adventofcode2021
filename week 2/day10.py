raw = open('input10.txt', 'r').read().split('\n')
#raw = open('test', 'r').read().split('\n')

end = [">", "]", "}", ")"]
begin = ["<", "[", "{", "("]

def delimiterErrorScore(char):
    if char == ">":
        return 25137
    elif char == ")":
        return 3
    elif char == "]":
        return 57
    elif char == "}":
        return 1197
    else:
        return 0

def getErrorScore(line):
    s = []
    s.append(line[0])
    if delimiterErrorScore(line[0]) != 0:
        return delimiterErrorScore(line[0])

    for c in line:
        if c not in end:
            s.append(c)
            continue
        if s[len(s)-1] == "(" and c != ")":
            print("expected ) but found " + c)
            return delimiterErrorScore(c)
        elif s[len(s)-1] == "(" and c == ")":
            s.pop()
        elif s[len(s)-1] == "[" and c != "]":
            print("expected ] but found " + c)
            return delimiterErrorScore(c)
        elif s[len(s)-1] == "[" and c == "]":
            s.pop()
        elif s[len(s)-1] == "{" and c != "}":
            print("expected } but found " + c)
            return delimiterErrorScore(c)
        elif s[len(s)-1] == "{" and c == "}":
            s.pop()
        elif s[len(s)-1] == "<" and c != ">":
            print("expected > but found " + c)
            return delimiterErrorScore(c)
        elif s[len(s)-1] == "<" and c == ">":
            s.pop()
    return 0

# part 1

sum = 0
for line in raw:
    sum += getErrorScore(line)
print(sum)
print("---")

# part 2

def delimiterScore(c):
    if c == ")":
        return 1
    elif c == "]":
        return 2
    elif c == "}":
        return 3
    elif c == ">":
        return 4
    return 0

def getAutoCompleteScore(line):
    s = []
    s.append(line[0])
    
    if line[0] in end:
        return 0
    for c in line:
        if c not in end:
            s.append(c)
            continue
        if s[len(s)-1] == "(" and c != ")":
            return 0
        elif s[len(s)-1] == "(" and c == ")":
            s.pop()
        elif s[len(s)-1] == "[" and c != "]":
            return 0
        elif s[len(s)-1] == "[" and c == "]":
            s.pop()
        elif s[len(s)-1] == "{" and c != "}":
            return 0
        elif s[len(s)-1] == "{" and c == "}":
            s.pop()
        elif s[len(s)-1] == "<" and c != ">":
            return 0
        elif s[len(s)-1] == "<" and c == ">":
            s.pop()
    # if len(s) != 0 then we need to finish string

    score = 0
    if len(s) != 1:
        while len(s) != 1:
            print(len(s))
            print("score: " + str(score))
            print("char: " + s[len(s)-1])
            if s[len(s)-1] == "(":
                s.pop()
                score *= 5
                score += delimiterScore(")")
                continue
            elif s[len(s)-1] == "[":
                s.pop()
                score *= 5
                score += delimiterScore("]")
                continue
            elif s[len(s)-1] == "{":
                s.pop()
                score *= 5
                score += delimiterScore("}")
                continue
            elif s[len(s)-1] == "<":
                s.pop()
                score *= 5
                score += delimiterScore(">")
                continue

        return score

print(getAutoCompleteScore("<{([{{}}[<[[[<>{}]]]>[]]"))
scores = []
for line in raw:
    if getErrorScore(line) == 0:
        scores.append(getAutoCompleteScore(line))
        pass
scores.sort()
median = len(scores)/2
print(scores[int(median)])