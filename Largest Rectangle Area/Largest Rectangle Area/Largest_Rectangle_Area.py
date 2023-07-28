
#Task -- Largest rectangle area from an array of different heights
def largestArea(barray):
    arraylen = len(barray)
    recArea = []
    flen = arraylen

    for l in range(arraylen):
        farea = 0
        farea = (barray[l] * flen)
        recArea.append(farea)
        flen -= 1
    return max(recArea)

def inputLen():
    num = int(input().strip())
    return num

def inputParam():
    barray = input().strip().split(" ")
    barray = list(map(int, barray))
    return barray

def inputIni():
    num = inputLen()
    barray = inputParam()
    cbit = inputCheck(num, barray)
    while not cbit:
        num = inputLen()
        barray = inputParam()
        cbit = inputCheck(num, barray)
    return barray

def inputCheck(num, barray):
    cbit = 1
    if len(barray) < 1 or len(barray) > pow(10,5):
        cbit = 0
    elif len(barray) != num:
        cbit = 0
    elif cbit:
        for l in range(len(barray)):
            if barray[l] < 1 or barray[l] > pow(10,6):
                cbit = 0
                break
    return cbit

a2 = inputIni()

#a = [1,2,3,4,5]
print(largestArea(a2))