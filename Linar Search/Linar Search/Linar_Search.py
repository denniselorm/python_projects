#Linear Search

def lsearch(array1, data):
    
    l = 0
    while array1[l] != data and l < len(array1):
        l += 1 

    if data == array1[l]:
        return l,data
    else:
         return "Data not found"

array1 = [2,3,9,5,6]

a,b = lsearch(array1, 9)
print("index", a)
print("data", b)
