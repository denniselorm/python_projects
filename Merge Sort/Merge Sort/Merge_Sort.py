import copy
#[2,4,3,5]
#j == 0
def nsort(array1):
    n = len(array1)
    if n == 1:
        return array1
    else:
        index1 = int(n/2)
        var1 = nsort(array1[:index1])
        var2 = nsort(array1[index1:n])
#    print(var1)
#    print(var2)
    return mergeArray(var1, var2) 

def mergeArray(a1,b1):
    c1 = []
    j = 0
    i = 0
 #   print(a1)
 #   print(b1)
    if a1 == 'None' or b1 == 'None':
        return
    else:
        while len(a1) != 0 and len(b1) != 0:
            if a1[j] < b1[i]:
                c1.append(a1[j])
#               print("ac1", c1)
                del a1[0]
            else:
                c1.append(b1[i])
#               print("b1", b1[i])
                del b1[0]

        while len(a1) != 0:
#           print("a1rem", a1)
            for j in range(len(a1)):
                c1.append(a1[j])
            break
        while len(b1) != 0:
#           print("b1rem", b1)
            for i in range(len(b1)):
                c1.append(b1[j])
            break
#    print("c1", c1)
    return c1
array1 = [7,6,4,2]
print(nsort(array1))
