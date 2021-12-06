# Sharon Lu
# Advent of Code
# Day 4 Part 1

# Constants
BOARD_SIZE = 5

# Function to replace called Number with an "X"
def markOffNums(dictBoard, calledNum):
    retDict = dictBoard
    for key in retDict.keys():
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if retDict[key][row][col] == calledNum:
                    retDict[key][row][col] = "X"
    return retDict

# Open Lines and Parse Values
fileLines = []
with open('day4input.txt', 'r') as f:
    for readline in f:
        fileLines.append(readline.rstrip('\n'))
drawnNums = fileLines[0]

# Create a dictionary of Bingo Boards
dictBingoBoards = {}
for i in range(int(len(fileLines)/BOARD_SIZE)):
    startingIndex = i*BOARD_SIZE+2
    dictBingoBoards[i] = fileLines[startingIndex: startingIndex+BOARD_SIZE]

# Iterate through drawn numbers
for i in range(len(drawnNums)):
    # Function to cross off numbers
    dictBingoBoards = markOffNums(dictBingoBoards, drawnNums[i])
print(dictBingoBoards)
    # Function to check for valid bingo cards     
