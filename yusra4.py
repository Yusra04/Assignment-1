newList = [12,35,9,56,34]

def swapList(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList

print("list after swapping:",swapList(newList))
