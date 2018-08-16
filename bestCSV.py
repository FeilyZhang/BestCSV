import csv

def bestCSV(fileName, indexList, *cleanFlag):
    
    nums = 1
    account = 1
    result = {}
    valueList = []

    # Open and read the file

    with open(fileName) as files:
        line = csv.reader(files)
        for value in indexList:
            for row in line:
                valueList.append(row[value])

    # Clean or reject invalid data

    for flag in range(0, len(cleanFlag) - 1):
        for num in range(0, len(valueList)):
            if valueList[num] == '' or valueList[num] == cleanFlag[flag]:
                valueList.pop(num)
    maxNum = len(valueList)

    # Data statistics

    while True:

        # When the list is not empty

        if maxNum != 0:

            # When a round of statistics does not reach the end of the list

            if nums != maxNum:
                if valueList[0] == valueList[nums]:
                    account += 1
                    valueList.pop(nums)
                    maxNum -= 1
                    result[valueList[0].split('.')[0]] = account
                else:
                    nums += 1
            # When a round of statistics reaches the end of the list

            else:

                # The last round of statistics may have only one list element left, 
                # so the element and its statistical results must be added to the dictionary before the element is popped.

                if maxNum == 1 and nums == 1:
                    result[valueList[0].split('.')[0]] = account
                    valueList.pop(0)
                    break

                # When not the last round of statistics for a list element or the last round of statistics, as usual

                else:
                    valueList.pop(0)
                    maxNum -= 1
                    nums = 1
                    account = 1

        # When the list is empty

        else:
            break
    return result
