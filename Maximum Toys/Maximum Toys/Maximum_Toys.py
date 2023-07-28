#Task return number of toys that can be bought given a list of them with prices and with a budget

def sort(array1):
    j = 0
    while j <= len(array1)-2:
        var1 = array1[j]
        i = j+1
        swapFlg = 0
        while i <= len(array1)-1:
            var2 = array1[i]
            if var1 > var2:
                var3 = var1
                array1[i-1] = var2
                array1[i] = var3
                swapFlg = 1
            var1 = array1[i]
            i += 1
        if swapFlg == 0:
            break
        j = 0
    return array1

def maxToys(array1, expen):
    array1 = sort(array1)
    price = 0
    toyCount = 0
    j = 0
    while j <= len(array1)-1:
        initCost = price + array1[j]
        if initCost <= expen:
            price += array1[j]
            toyCount += 1
        else:
            break
        j += 1
    return toyCount

def inputParam():
    sizeTgt = input().strip().split(" ")
    sizeTgt = list(map(int,sizeTgt))
    return sizeTgt

def inputList():
    listCst = input().strip().split(" ")
    listCst = list(map(int,listCst))
    return listCst

def inputCon():
    sizeTgt = inputParam()
    listCst = inputList()
    cbit = inputCheck(sizeTgt, listCst)
    while not cbit:
        sizeTgt = inputParam()
        listCst = inputList()
        cbit = inputCheck(sizeTgt, listCst)
    return listCst,sizeTgt

def inputCheck(sizeTgt, listCst):
    cbit = 1
    if len(listCst) != sizeTgt[0]:
        cbit = 0
    elif sizeTgt[0] < 1 or sizeTgt[0] > pow(10,5):
        cbit = 0
    elif sizeTgt[1] < 1 or sizeTgt[1] > pow(10,9):
        cbit = 0
    elif cbit:
        for i in range(len(listCst)):
            if listCst[i] < 1 or listCst[i] > pow(10,9):
                cbit = 0
                break
    return cbit


#a = [6,4,1,2,3,2,1]
#print(sort(a))
#maxToys(a,7)
#a = [1,2,3,4]

a,b = inputCon()
print(maxToys(a,b[1]))
