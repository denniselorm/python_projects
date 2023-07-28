
# 1 2 3 4 5
#Task -- Find the maximum value of a minimum set for a range of distinct artifact sizes

def artftMinMax(array1):
    maxVal = {}
    l = 0
    while l < len(array1):
        n = 0
        var2 = []
        while n < len(array1)-1:
            if l == 0:
                var2 = []
                for m in range(len(array1)):
                    var2.append(array1[m])
                break
#                maxVal[l+1] = max(var)
            else:
                var = []
                if n+l+1 <= len(array1):
                    for m in range(n,n+l+1):
                        var.append(array1[m])
            if len(var) == l+1:
                var2.append(min(var))
            n += 1
        maxVal[l+1] = max(var2)
        l += 1
    for itemVal in maxVal.values():
        print(itemVal, end=" ")
    print("")

def inputLen():
    llen = int(input().strip())
    return llen

def inputParam():
    listvar = input().strip().split(" ")
    listvar = list(map(int, listvar))
    return listvar

def inputInit():
    llen = inputLen()
    listvar = inputParam()
    cbit = inputCheck(llen, listvar)
    while not cbit:
        llen = inputLen()
        listvar = inputParam()
        cbit = inputCheck(llen, listvar)
    return listvar

def inputCheck(llen, listvar):
    cbit = 1
    if llen < 1 or llen > pow(10,6):
        cbit = 0
    elif cbit:
        for l in range(len(listvar)):
            if listvar[l] < 0 or listvar[l] > pow(10,9):
                cbit = 0
                break
    return cbit

a = inputInit()
#a = [2,6,1,12]
artftMinMax(a)
