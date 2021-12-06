f = open('day1input.txt', 'r')
fList = f.readlines()
dictWindow = {}
for i in range(len(fList)-2):
    dictWindow[i] = 0
    for index in range(i, i+3):
        dictWindow[i] += int(fList[index])
lastVal = dictWindow[0]
totalCount = 0
for key in dictWindow.keys():
    if lastVal < dictWindow[key]:
        totalCount += 1
    lastVal = dictWindow[key]
print(totalCount)
f.close()

