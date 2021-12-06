# Sharon Lu
# Advent of Code 2021
# Day 3

#open file and store values without new line in fileLines
fileLines = []
with open('day3input.txt', 'r') as f:
    for readLine in f:
        fileLines.append(readLine.rstrip())

# Create Dictionary for differences and initialize
dictDifferences = {}
for i in range(len(fileLines[0].rstrip())):
    dictDifferences[i] = 0

# Iterate through each line
for line in fileLines:
    #Iterate through each binary digit
    for i in range(len(line)):
        if line[i] == '0':
            dictDifferences[i] -= 1
        elif line[i] == '1':
            dictDifferences[i] += 1

# Create Gamma Rate Based on differences
gammaRateStr = ""
for i in range(len(dictDifferences)):
    if dictDifferences[i] > 0:
        gammaRateStr += "1"
    else:
        gammaRateStr += "0"
gammaRateInt = int(gammaRateStr, 2)

#Flip Gamma Rate Bits
epsilonRateStr = ""
for i in range(len(gammaRateStr)):
    if gammaRateStr[i] == "0":
        epsilonRateStr += "1"
    else:
        epsilonRateStr += "0"
epsilonRateInt = int(epsilonRateStr, 2)
print(gammaRateInt*epsilonRateInt)
