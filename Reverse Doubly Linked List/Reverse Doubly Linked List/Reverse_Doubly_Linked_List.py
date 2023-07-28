
#Task -- Reverse a doubly linked list
#First input -- number of test cases e.g{1}
#Second input -- LinkedList length n e.g{2}
#Next n lines -- Linkedlist elements


#Linkedlist Node class
class Node:
    def __init__(self, data=None):
        self.data = data 
        self.next = None
        self.prev = None


#Doubly linkedlist class with reverse function
class Dllist:
    def __init__(self, head=None):
        self.head = head
        self.first = None
        self.last = None

    def printList(self):
        link = self.head
        while link != None:
            print(link.data, end=" ")
            link = link.next
        print("")

    def insertEnd(self, node):
        link = self.head
        if link == None:
            self.head = node

        else:
             while link.next != None:
                 link = link.next
             node.next = link.next
             link.next = node
             node.prev = link

    def reverseList(self):
        link = self.head
        prev = None
        if link == None:
            return
        else:
            while link.next != None:
                var = link.next
                link.next = prev
                prev = link
                link.prev = var
                link = var
            link.next = prev
            self.head = link


#Query user for number of testcases
def testCase():
    tcase = int(input().strip())
    return tcase


#Queries user for linklist length and linkedlist elements for each test case
def llInfo(tcase):
    lldict = {}
    dlist = []
    
    for l in range(tcase):
        llen = int(input().strip())
        dldata = []
        dlist = []
        for n in range(llen):
            dldata.append(int(input().strip()))
        dlist.append(dldata)
        dldata = []
        dldata.append(llen)
        dlist.append(dldata)
        lldict[l+1] = dlist
    return lldict


#Calls testCase, llInfo functions and passes return values to inputCheck
#Creates node objects for each data element, inserts into position & reverses the linkedlist
def dlInit():
    tcase = testCase()
    lldict = llInfo(tcase)
    llnameList = []
    llvalue = list(lldict.values())
    cbit = inputCheck(tcase, lldict)

    while not cbit:
        tcase = testCase()
        lldict = llInfo(tcase)
        l1 = Dllist()
        llvalue = list(lldict.values)
        cbit = inputCheck(tcase, lldict)

    for n in range(len(llvalue)):
        llname = "l" + str(n+1)
        llname = Dllist()
        for l in range(len(llvalue[n])):
            lldata = llvalue[n][l]
            for k in range(len(lldata)):
                if l == 1:
                    pass
                else:
                    objname = "obj" + str(l) + str(k)
                    objname = Node(lldata[k])
                    llname.insertEnd(objname)
        llname.reverseList()
        llnameList.append(llname)
#        llname.printList()
    return llnameList


#Check validity of user inputs against validity
def inputCheck(tcase, lldict):
    cbit = 1
    llvalue = list(lldict.values())
    if tcase < 1 or tcase > 10:
        cbit = 0
    else:
        for n in range(len(llvalue)): 
            for l in range(len(llvalue[n])):
                lldata = llvalue[n][l]
                for k in range(len(lldata)):
                    if l == 0:
                        if lldata[k] < 0 or lldata[k] > 1000:
                            cbit = 0
                            break
                    else:
                        if lldata[k] < 0 or lldata[k] > 1000:
                            cbit = 0
                            break
    return cbit


#########################################################################################
###### Main Code block ##################################################################

llnameList = dlInit()
for l in range(len(llnameList)):
    llnameList[l].printList()

'''
a1 = Node(10)
l1 = Dllist(a1)
a2 = Node(20)
l1.insertEnd(a2)
a3 = Node(30)
a4 = Node(40)
l1.insertEnd(a3)
l1.insertEnd(a4)
l1.printList()
l1.reverseList()
l1.printList()
'''