# Sharon Lu
# Advent of Code
# Day 4 Part 2

### Constants
BOARD_SIZE = 5

### Helper Functions
# Function to replace ther Drawn Number with an "X"
def markOffNums(dictBoard, drawnNum):
    retDict = dictBoard
    for key in retDict.keys():
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if retDict[key][row][col] == drawnNum:
                    retDict[key][row][col] = "X"
    return retDict
    
def checkForBingo(bingoBoard):
    # Check Rows
    for row in range(BOARD_SIZE):
        if bingoBoard[row][0] == "X":
            isBingo = True
            for col in range(BOARD_SIZE):
                if bingoBoard[row][col] != "X":
                    isBingo = False
                    break
            if isBingo == True:
                return True
    # Check Columns
    for col in range(BOARD_SIZE):
        if bingoBoard[0][col] == "X":
            isBingo = True
            for row in range(BOARD_SIZE):
                if bingoBoard[row][col] != "X":
                    isBingo = False
                    break
            if isBingo == True:
                return True
    return False
    
def calculateBoardSum(bingoBoard):
    total = 0
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if bingoBoard[row][col] != "X":
                total += int(bingoBoard[row][col])
    return total


### Main Program
# Open Lines and Parse Values
fileLines = []
with open('day4input.txt', 'r') as f:
    for readline in f:
        fileLines.append(readline.strip().rstrip('\n').split())
drawnNums = fileLines[0][0].split(",")

# Create a dictionary of Bingo Boards
dictBingoBoards = {}
for i in range(int(len(fileLines)/(BOARD_SIZE+1))):
    startingIndex = i*BOARD_SIZE+i*1+2
    dictBingoBoards[i] = fileLines[startingIndex: startingIndex+BOARD_SIZE]

# Iterate through drawn numbers
finalBingo = False
for i in range(len(drawnNums)):
    # Function to cross off numbers
    dictBingoBoards = markOffNums(dictBingoBoards, drawnNums[i])
    keysToPop = []
    # Function to check for valid bingo cards
    for key in dictBingoBoards.keys():
        if checkForBingo(dictBingoBoards[key]) == True:
            keysToPop.append(key)
            if len(dictBingoBoards) == 1:
                boardSum = calculateBoardSum(dictBingoBoards[key])
                finalBingo = True
    for popKey in keysToPop:
        dictBingoBoards.pop(popKey)
    if finalBingo == True:
        break
print(int(boardSum)*int(drawnNums[i]))

