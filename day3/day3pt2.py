# Sharon Lu
# Advent of Code 2021
# Day 3 Part 2


def maxBinaryVals(listStrings):
    # Create Dictionary for differences and initialize
    dictDifferences = {}
    for i in range(len(listStrings[0])):
        dictDifferences[i] = 0

    # Iterate through each line
    for line in listStrings:
        #Iterate through each binary digit
        for i in range(len(line)):
            if line[i] == '0':
                dictDifferences[i] -= 1
            elif line[i] == '1':
                dictDifferences[i] += 1
                
    # Create String of Maxes
    maxValString = ""
    for i in range(len(dictDifferences)):
        if dictDifferences[i] >= 0:
            maxValString += "1"
        elif dictDifferences[i] < 0:
            maxValString += "0"
    return maxValString

def reducedList(listStrings, bitToEvaluate, maxValString):
    maxBinary = maxValString[bitToEvaluate]
    retList = []
    for binaryString in listStrings:
        if binaryString[bitToEvaluate] == maxBinary:
            retList.append(binaryString)
    
    return retList

def invertBinaryString(binaryString):
    retString = ""
    for i in range(len(binaryString)):
        if binaryString[i] == "1":
            retString += "0"
        else:
            retString += "1"
    return retString
    
    
#open file and store values without new line in fileLines
fileLines = []
with open('day3input.txt', 'r') as f:
    for readLine in f:
        fileLines.append(readLine.rstrip())
        
# Get reading for oxygen
listStrings = fileLines    
for i in range(len(fileLines[0])):
    maxVals = maxBinaryVals(listStrings)
    listStrings = reducedList(listStrings, i, maxVals)
oxygenrating = int(listStrings[0],2)
        
# Get reading for CO2
listStrings = fileLines    
for i in range(len(fileLines[0])):
    maxVals = maxBinaryVals(listStrings)
    minVals = invertBinaryString(maxVals)
    listStrings = reducedList(listStrings, i, minVals)
    if len(listStrings) == 1:
        break
corating = int(listStrings[0],2)
print(oxygenrating*corating)
