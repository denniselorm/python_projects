# Task move integer in array towards end of array based on d i.e. [1,2,3,4,5] --> [2,3,4,5,1] when d=1
# 1 <= n <= 10^5
# 1 <= d <= n
# 1 <= a[i] <= 10^6

def rotLInteger(array1):
    temp = array1[0]
    del array1[0]
    array1.append(temp)
    return array1

def iterRotInteger(array1, d):
    array2 = []
    for i in range(d):
        array2 = rotLInteger(array1)

#    array2 = list(map(str,array2))
#    array2 = " ".join(array2)
#    return array2
    for i in range(len(array2)):
        print(array2[i], end=" ")
    print("")

def inputParam():
    opParam = input().strip().split(" ")
    opParam = list(map(int,opParam))
    arrayLen = opParam[0]
    opRep = opParam[1]
    return arrayLen, opRep

def inputList():
#    arrayLen, opRep = inputParam()
    array1 = input().strip().split(" ")
    array1 = list(map(int,array1))
    return array1

def inputQueryCon():
    arrayLen, opRep = inputParam()
    array1 = inputList()
    checkBit = inputQueryCheck(arrayLen, opRep, array1)
    while not checkBit:
        print("Enter new set of inputs: ")
        arrayLen, opRep = inputParam()
        array1 = inputList()
        checkBit = inputQueryCheck(arrayLen, opRep, array1)
    return array1, opRep

def inputQueryCheck(arrayLen, opRep, array1):
    checkBit = 1
    if len(array1) != arrayLen:
        checkBit = 0
    if opRep < 1 or opRep > arrayLen:
        checkBit = 0
    if arrayLen < 1 and arrayLen > pow(10,5):
        checkBit = 0
    if True:
        for i in range(len(array1)):
            if array1[i] < 1 or array1[i] > pow(10,6):
                checkbit = 0
                break
    if checkBit:
        return 1
    else:
        return checkBit
#a = [2,3,4,5,6]
#d = 2
a,d = inputQueryCon()
iterRotInteger(a, d)



