import copy 

def ttlSpan(array1):
    array2 = copy.copy(array1)
    l = 0
    dcount = 0
    while l < len(array2):
        n = 0 
        var = []
        contntf = 0
        while n < len(array2)-1:
            if n+1 < len(array2):
                if array2[n] < array2[n+1]:
                    var.append(array2[n+1])
                    contntf += 1
            n += 1
        if contntf == 0:
            break
        for m in range(len(var)):
            array2.remove(var[m])
        dcount += 1
        l = 0
    return dcount

def inputLen():
    llen = int(input().strip())
    return llen

def inputParam():
    var = input().strip().split(" ")
    var = list(map(int, var))
    return var

def inputInit():
    llen = inputLen()
    var = inputParam()
    cbit = inputCheck(llen, var)
    while not cbit:
        llen = inputLen()
        var = inputParam()
        cbit = inputCheck(llen, var)
    return var

def inputCheck(llen, var):
    cbit = 1
    if llen < 1 or cbit > pow(10,5):
        cbit = 0
    elif cbit:
        for l in range(len(var)):
            if var[l] < 0 or var[l] > pow(10,9):
                cbit = 0
                break
    return cbit

#a = [6,5,8,4,7,10,9]
b = [3,6,2,7,5]
c = inputInit()
print(ttlSpan(c))
