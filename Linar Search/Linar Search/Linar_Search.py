#Implement the linear search function
#First input line --- Values of array elements; space separated e.g. {2 3 6 9 10}
#Second input line --- Value to be searched for e.g {2}


#Linear search function
def lsearch(array1, data):
    l = 0
    while array1[l] != data and l < len(array1):
        l += 1
    if data == array1[l]:
        return l,data
    else:
         return "Data not found"

#Queries user for array values and value to be searched for
def inputVal():
    alist = input().strip().split(" ")
    alist = list(map(int,alist))
    valsearch = int(input().strip())

    return alist, valsearch

#######################################################################################################################
############# Main Block of Code ######################################################################################

array1, valsearch = inputVal()
a,b = lsearch(array1, 9)
print("Data", b, "found at index", a)





#Extra test cases
array1 = [2,3,9,5,6]

