def swapList(newList):
    newList[0],newList[-1] = newList[-1],newList[0]
    return newList
newList = [1,2,3,4,5]
print(swapList(newList))

def swapList(list):
    get = list[-1], list[0]
    list[0], list[-1] = get
    return list
newList = [1,2,3,4,5]
print(swapList(newList))

def swaplist(list):
    start,*middle,end = list
    list = [end,*middle,start]
    return list
newList = [1,2,3,4,5,6,7,8]
print(swapList(newList))




