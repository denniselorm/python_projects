
# Task -- return minimum number of deletions to form anagrams of two strings 

#cde
#dcf

def formAnagram(str1, str2):
    if len(str1) < len(str2):
        temp = str1
        str1 = str2
        str2 = temp
    temp1 = " ".join(str1)
    temp1 = temp1.split(" ")
    temp2 = " ".join(str2)
    temp2 = temp2.split(" ")
    temp3 = []
    j = 0
    i = 0
    mCount = 0
    while j <= len(temp1)-1:

        while i <= len(temp2)-1:
            if temp1[j] == temp2[i]:
                del temp1[j]
                del temp2[i]
                j = -1
                i = 0
                mCount += 1
                break
            elif temp1[j] != temp2[i] and i == len(temp2)-1:
                temp3.append(temp1[j])
                del temp1[j]
                j = -1
                i = 0
                break
            i += 1
        if len(temp2) == 0:
            for k in range(len(temp1)):
                temp3.append(temp1[k])
            break
        j += 1
    if len(temp2) != 0:
        for k in range(len(temp2)):
            temp3.append(temp2[k])

    print(temp3)
    if mCount == 0:
        print("Cannot generate anagrams from the two provided strings")
    else:
        return (len(temp3))

def userInput():
    input1 = input().strip()
    input2 = input().strip()
    return input1, input2

def userInputCon():
    input1, input2 = userInput()
    checkBit = inputQueryCheck(input1, input2)
    while not checkBit:
        input1, input2 = userInput()
        checkBit = inputQueryCheck(input1, input2)
    return input1, input2

def inputQueryCheck(input1, input2):
    checkBit = 1
    if len(input1) < 1:
        checkBit = 0
    elif len(input2) > pow(10,4):
        checkBit = 0
    return checkBit

#a = "cde"
#b = "dcf"
#a = "abcfeg" #bcfeg cfeg feg eg g af
#b = "bce"    #bce   ce    e  e  []
a, b = userInputCon()
print(formAnagram(a,b))
      
    




