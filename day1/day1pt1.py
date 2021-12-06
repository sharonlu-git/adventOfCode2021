f = open('day1input.txt', 'r')
fList = f.readlines()
lastReading = int(fList[0])
totalCount = 0
for reading in fList:
    if int(reading) > lastReading:
        totalCount = totalCount + 1
    lastReading = int(reading)
print(totalCount)
f.close()
