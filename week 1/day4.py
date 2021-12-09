data = open('input4.txt', 'r').read().split('\n\n')
#data = open('test', 'r').read().split('\n\n')


# part 1
numbers = data[0].split(',')

def getInt(str):
    return int(str)

def getUnmarkedNums(nums, index, board):
    sum = 0
    markedNums = []
    for i in range(index+1):
        markedNums.append(nums[i])
    for row in board:
        r = row.split(' ')
        for c in r:
            if c not in markedNums:
                sum += getInt(c)
    return sum


def doesBoardWin(nums, inp):
    board = inp.split('\n')
    numIndex = 0
    answer = 0
    bitboard = [[0 for x in range(5)] for y in range(5)]
    for n in nums:
        for i in range(5):
            row = board[i].split(' ')
            for j in range(5):
                if row[j] == n:
                    bitboard[i][j] = 1
        
        # win condition

        # check row
        for i in range(5):
            sum = 0
            for j in range(5):
                sum += bitboard[i][j]
            if sum == 5:
                # get sum of unmarked numbers
                answer += getUnmarkedNums(nums, numIndex, board)
                answer *= getInt(nums[numIndex])
                return [numIndex, answer]
        
        # check columns
        for i in range(5):
            sum = 0
            for j in range(5):
                sum += bitboard[j][i]
            if sum == 5:
                # get sum of unmarked numbers
                answer += getUnmarkedNums(nums, numIndex, board)
                answer *= getInt(nums[numIndex])
                return [numIndex, answer]
        numIndex += 1


arr = doesBoardWin(numbers, data[3])
answer = -1
min = 9123123123
for i in range(1,len(data)):
    if doesBoardWin(numbers, data[i])[0] < min:
        answer = doesBoardWin(numbers, data[i])[1]
        min = doesBoardWin(numbers, data[i])[0]
        print("new answer: " + str(answer) + " found at index " + str(min))
print("final answer: " + str(answer))
print("---")

# part 2

answer = -1
max = -1
for i in range(1,len(data)):
    if doesBoardWin(numbers, data[i])[0] > max:
        answer = doesBoardWin(numbers, data[i])[1]
        max = doesBoardWin(numbers, data[i])[0]
        print("new answer: " + str(answer) + " found at index " + str(max))
print("final answer: " + str(answer))