
#Task find the maximum sum modulo i.e sum[array] % m given array and m

# 2 4 5 6
def maxSumModulo(array1, modul):
    modSum = {}
    j = 0
    varArray = []
    var = 0
    dkey = 1

    while j in range(len(array1)):
        for i in range(len(array1)):
            if j == 0:
                var = array1[i]
            else:
                var = 0
                varArray = array1[i:j+i+1]
                if len(varArray) == j+1:
                    for k in range(len(varArray)):
                        var += varArray[k]
                else:
                    break
            modSum[dkey] = var % modul
            dkey += 1
        j += 1
    value = modSum.values()
    return(max(value))

def queryNum():
    qnum = int(input().strip())
    return qnum

def queryInfo(qnum):
    input1 = []
    array1 = []
    array2 = []
    qdict = {}
    for j in range(qnum):
        array2 = []
        input1 = input().strip().split(" ")
        input1 = list(map(int,input1))
        array1 = input().strip().split(" ")
        array1 = list(map(int,array1))
        array2.append(input1)
        array2.append(array1)
        qdict[j+1] = array2
    return qdict

def queryCon():
    qnum = queryNum()
    qdict = queryInfo(qnum)
    checkBit = queryCheck(qnum, qdict)
    while not checkBit:
        qnum = queryNum()
        qdict = queryInfo(qnum)
        checkBit = queryCheck(qnum, qdict)
    return qnum, qdict

def queryCheck(qNum, qdict):
    checkBit = 1
    for v in qdict.values():
        dictValue = v
        if dictValue[0][0] < 1 or dictValue[0][0] > pow(10,5):
            checkBit = 0
        elif dictValue[0][1] < 1 or dictValue[0][1] > pow(10,14):
            checkBit = 0
        elif checkBit:
            for k in range(len(dictValue)):
                if dictValue[1][k] < 1 or dictValue[1][k] > pow(10,18):
                    checkBit = 0
    return checkBit

a = [3,3,9,9,5]
#print(maxSumModulo(a, 2))

qnum, qdict = queryCon()

for v in qdict.values():
    dictv = v
    print(maxSumModulo(dictv[1], dictv[0][1]))
