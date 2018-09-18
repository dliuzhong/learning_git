def max(colWidthslist):
    if len(colWidthslist) == 0:
        return 0
    maxWidth = colWidthslist[0]
    for i in range(len(colWidthslist)):
        if i == 0:
            continue
        if maxWidth < colWidthslist[i]:
            maxWidth = colWidthslist[i]
    return maxWidth

def maxWords(tableData):
    if len(tableData) == 0:
        return 0
    maxWidth = len(tableData[0])
    for i in range(len(tableData)):
        if i == 0:
            continue
        if maxWidth < len(tableData[i]):
            maxWidth = len(tableData[i])
    return maxWidth

def maxWordWidth(colList):
    if len(colList) == 0:
        return 0
    maxWidth = len(colList[0])
    for i in range(len(colList)):
        if i == 0:
            continue
        if maxWidth < len(colList[i]):
            maxWidth = len(colList[i])
    return maxWidth

tableData = [['apples', 'oranges', 'cherries', 'banana', 'apples'], ['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose', 'maomaoshijin', 'meimei']]
colWidths = [0] * len(tableData)
for i in range(len(tableData)):
    colWidths[i] = maxWordWidth(tableData[i])
maxWidth = max(colWidths)
maxWords = maxWords(tableData)
lenTable = len(tableData)
for i in range(maxWords):
    for j in range(lenTable):
        try:
            print(str(tableData[j][i]).rjust(maxWidth), end='')
        except:
            print(''.rjust(maxWidth), end='')
        if j < (lenTable - 1):
            print(' ', end='')
        else:
            print('')


