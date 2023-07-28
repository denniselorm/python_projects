# Task -- Find maximum sum of a subset of non adjacent elements
# -2 -1 3 -4 5 
def maxSubSum(array1):
    l = 0
    dictsum = {}
    dictCount = 1
    while l < len(array1)-2:
        n = l+2
        var2 = []
        var = []

        for m in range(l,len(array1),2):
            var2.append(array1[m])

        while n <= len(array1)-1:
            pemt = []
            pemt.append(array1[l])
            pemt.append(array1[n])
            var.append(pemt)

            dictsum[dictCount] = array1[l] + array1[n]
            dictCount += 1
            n += 1
        if var2 not in var:
            var3 = 0
            for s in range(len(var2)):
                var3 += var2[s]
            dictsum[dictCount] = var3
            dictCount += 1
        l += 1
    dictvalues = list(dictsum.values())
    return max(dictvalues)

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
    if llen < 1 or llen > pow(10,5):
        cbit = 0

    elif cbit:
             for l in range(len(listvar)):
                if listvar[l] < (-1 * pow(10,4)) or listvar[l] > pow(10,4):
                    cbit = 0
                    break
    return cbit
                    
#arr = [-2,1,3,-4,5]
arr = inputInit()
print(maxSubSum(arr))

