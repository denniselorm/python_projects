
#Task -- Largest rectangle area from an array of different heights given the heights as array values
#First input line -- Integer value of array size e.g {2 or 3 or 6}
#Second input line -- Values of area representing the heights; space separated e.g. {2 3 6 7 9}


#Returns the largest array area
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


#Queries user for total width/size of arrray/area
def inputLen():
    num = int(input().strip())
    return num


#Queries user for array values representing the heights
def inputParam():
    barray = input().strip().split(" ")
    barray = list(map(int, barray))
    return barray


#Calls inputLen, inputParam functions and return call values to inputCheck function
def inputIni():
    num = inputLen()
    barray = inputParam()
    cbit = inputCheck(num, barray)
    while not cbit:
        num = inputLen()
        barray = inputParam()
        cbit = inputCheck(num, barray)
    return barray


#Checks validity of user input against constraints
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


#####################################################################################################
####### Main Block of Code ###########################################################################
a2 = inputIni()
print(largestArea(a2))


#Extra test case
#a = [1,2,3,4,5]
