
# Task #1 if '1' append element d if #2 delete first occurence of element d  #3 Check d frequency of element in form [{123}, d]

def userOperation(array1):
    op = array1[0]
    ele = array1[1]
    array2 = []

    for j in range(len(array1)):
        op = array1[j][0]
        ele = array1[j][1]
        if op == 1:
            array2.append(ele)
        if op == 2:
            if ele in array2:
                array2.remove(ele)
        if op == 3:
            opdict = {}
            for i in range(len(array2)):
                eleKeys = opdict.keys()
                if array2[i] in eleKeys:
                    opdict[array2[i]] += 1
                else:
                    opdict[array2[i]] = 1
            dictValue = opdict.values()
            if ele in dictValue:
                print(1)
            else:
                print(0)
 #   print(array2)

def userInput1():
    opNum = int(input().strip())
    return opNum

def userInput2(opNum):
    opArray = []
    for j in range(opNum):
        input1 = input().strip().split(" ")
        input1 = list(map(int, input1))
        opArray.append(input1)
    return opArray

def userInputCon():
    opNum = userInput1()
    opArray = userInput2(opNum)
    checkBit = userInputCheck(opNum, opArray)
    while not checkBit:
        opNum = userInput1()
        opArray = userInput2()
        checkBit = userInputCheck(opNum, opArray)
    return opArray

def userInputCheck(opNum, opArray):
    checkBit = 1
    if opNum < 1 or opNum > pow(10,5):
        checkBit = 0
    elif True:
        pass
        for j in range(len(opArray)):
            if opArray[j][0] < 1 or opArray[j][0] > pow(10,9):
                checkBit = 0
                break
            if opArray[j][1] < 1 or opArray[j][1] > pow(10,9):
                checkBit = 0
                break
    return checkBit

#a = [[1,2], [1,2], [1,2], [2,2], [3,2]]
a = userInputCon()
userOperation(a)
