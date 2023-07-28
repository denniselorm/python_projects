
## Task -- Inplement the selection sort algorithm and return sorted array

# Sorts array using selection sort logic
def sort(array1):
    temp = 0
    for i in range(len(array1)-1):
        j = i + 1
        swapped = 0
        temp = array1[i]
        swapIndex = -1
        while j <= len(array1)-1:
            if temp > array1[j]:
                temp = array1[j]
                swapped = 1
                swapIndex = j
            j += 1

        if temp < array1[i]:
            del array1[swapIndex]
            array1.insert(i, temp)

        if temp == array1[i] and not swapped:
            pass
    print(array1)
    print("-------->")


###########################################################################################################
####### Main code block ###################################################################################

b = [3,1,4,6,9,2,12,5]
a = [2,1,4,3]
c = [2,4,3,1,2,7,5]
d = [2,1,11,4,4,0,7,3]

for i in (a,b,c,d):
    sort(i)

'''
#print("2,1,4,3,2")
# 1,2,4,3,4 i=0 j=1
# 1,2,4,3,4 i=1 j=2
# 1,2,3,4,4 i=2 j=3
'''