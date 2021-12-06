f = open('day2input.txt', 'r')
fileLines = f.readlines()
verticalPos = 0
horizontalPos = 0
for line in fileLines:
    lineSplit = line.split()
    if lineSplit[0] == "forward":
        horizontalPos += int(lineSplit[1])
    elif lineSplit[0] == "down":
        verticalPos += int(lineSplit[1])
    elif lineSplit[0] == "up":
        verticalPos -= int(lineSplit[1])
print(verticalPos * horizontalPos)
f.close()
