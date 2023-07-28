
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None

class Dllist:
    def __init__(self, head=None):
        self.head = head
        self.last = None
        self.nodeCount = 0
    
    def printList(self):
        link = self.head
        while link != None:
            print(link.data, end=" ")
            link = link.next
        print("")

    def insertNodeSort(self, node):
        link = self.head
        if link.data > node.data:
            node.next = self.head
            self.head = node
            self.nodeCount += 1
        else:
            self.nodeCount = 0
            while node.data > link.data:
                if link.next != None:
                    prev = link
                    link = link.next
                    self.nodeCount += 1
                else:
                    break

            if link.next != None:
                node.next = prev.next
                prev.next = node
                node.prev = prev
                self.nodeCount += 1
            elif link.next == None and link.data > node.data:
                node.next = prev.next
                prev.next = node
                node.prev = prev
                self.nodeCount += 1
            elif link.next == None and link.data < node.data:
                node.next = link.next
                link.next = node
                node.prev = link
                self.nodeCount += 1

    def insertEnd(self, node):
        link = self.head
        if link == None:
            self.head = node
            self.nodeCount = 0
        else:
            while link.next != None:
                link = link.next
            node.next = link.next
            link.next = node
            node.prev = link
            self.nodeCount += 1

    def sort(self):
        link = self.head
        while link.next != None:
            link2 = link.next
            swp = 0
            while link2 != None:
                if link.data > link2.data:
                    if link == self.head:
                        link3 = link
                        self.head = link2
                        link3.next = link2.next
                        link2.next = link3
                        link3.prev = link2
                        swp = 1
                    elif link2.next == None:
                        link3 = link2
                        link.next = None
                        link3.next = prev.next
                        prev.next = link3
                        link3.prev = prev 
                        swp = 1
                    else:
                        link3 = link2
                        if link2.next != None:
                            link4 = link2.next
                            link.next = link2.next
                            link4.prev = link
                        else:
                            link.next = link2.next
                        link3.next = prev.next
                        prev.next = link3
                        link3.prev = prev 
                        swp = 1
                prev = link
                link = link2
                link2 = link.next
            if swp == 0:
                break
            link = self.head
                         
def testCase():
    tcase = int(input().strip())
    return tcase

def dlData(tcase):
    dldict = {}
    lldata = []
    ldlist = []
    datalen = []
    for l in range(tcase):
        llen = int(input().strip())
        datalen.append(llen)
        for n in range(llen):
            lldata.append(int(input().strip()))
        ldlist.append(lldata)
        lldata = []
        for j in range(1):
            lldata.append(int(input().strip()))
        ldlist.append(lldata)
        dldict[l+1] = ldlist
        lldata = []
        ldlist = []
    return dldict, datalen

def dlinit():
    tcase = testCase()
    dldict, datalen = dlData(tcase)
    cbit = inputCheck(tcase, dldict, datalen)

    while not cbit:
        tcase = testCase()
        dldict = dlData(tcase)
        cbit = inputCheck(tcase, dldict, datalen)

    llvalue = list(dldict.values())
    for n in range(len(llvalue)):        
            for l in range(len(llvalue[n])):
                lldata = llvalue[n][l]
                for j in range(len(lldata)):
                    objname = "obj" + str(n)
                    if l == 0:
                        if j == 0:
                            objname = Node(lldata[j])
                            l1 = Dllist(objname)
                        else:
                            objname = Node(lldata[j])
                            l1.insertEnd(objname)
                    if l == 1:
                        l1.sort()
                        objname = Node(lldata[j])
                        l1.insertNodeSort(objname)                
    return l1

def inputCheck (tcase, dldict, datalen):
    cbit = 1
    if tcase < 1 or tcase > 10:
        cbit = 0
    elif cbit:
        llvalue = list(dldict.values())
        for n in range(len(llvalue)):
            if cbit == 0:
                break
            tlist = llvalue[n]
            for l in range(len(tlist)):
 #               if l == 0:
 #                   n = len(llvalue)
 #                   if n < 1 or n > 1000:
 #                       cbit = 0
 #                       break
                lldata = llvalue[n][l]
                for j in range(len(lldata)):
                    if lldata[j] < 1 or lldata[j] > 1000:
                        cbit = 0
                        print(lldata[j])
                        print('n', n, 'l', l, 'j', j)
                        break
    elif cbit:
            for l in range(len(datalen)):
                if datalen[l] < 1 or datalen[l] > 1000:
                    cbit = 0
                    break
    return cbit


l1 = dlinit()
l1.printList()

'''
a1 = Node(30)
dl1 = Dllist(a1)
a2 = Node(20)
dl1.insertEnd(a2)
a3 = Node(50)
a4 = Node(60)
a5 =  Node(15)
dl1.insertEnd(a3)
dl1.insertEnd(a4)
dl1.insertEnd(a5)
dl1.sort()
a6 = Node(55)
a7 = Node(10)
a8 = Node(65)
dl1.insertNodeSort(a6)
dl1.insertNodeSort(a7)
dl1.insertNodeSort(a8)
dl1.printList()
        '''