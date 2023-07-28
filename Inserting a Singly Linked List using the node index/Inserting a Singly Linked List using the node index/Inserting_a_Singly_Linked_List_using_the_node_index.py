
#Task -- Create a a linked list with n elements and insert new node at position pos
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Sllist:
    def __init__(self, head=None):
        self.head = head
        self.nodeCount = 0 

    def printList(self):
        link = self.head
        while link != None:
            print(link.data, end=" ")
            link = link.next
        print("")
    
    def insertBeforeNode(self, node, ncount):
        link = self.head
        prev = None
        if link == None:
            self.head = node
            self.nodeCount = 0
        elif self.nodeCount == 0:
            node.next = link
            self.head = node
            self.nodeCount += 1
        else:
            self.nodeCount = 0
            while link != 0 and self.nodeCount != ncount:
                prev = link
                link = link.next
                self.nodeCount += 1
            node.next = prev.next
            prev.next = node
            node.next = link

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
            self.nodeCount += 1

def nodeNum():
    nodenum = int(input().strip())
    return nodenum 

def nodeEle(nodenum):
    nodeele = []
    newdata = []
    for l in range(nodenum):
        usernode = int(input().strip())
        nodeele.append(usernode)

    usernode2 = int(input().strip())
    newdata.append(usernode2)
    usernode2 = int(input().strip())
    newdata.append(usernode2)

    return nodeele, newdata

def listIni():
    nodenum = nodeNum()
    nodeele, newdata = nodeEle(nodenum)   
    cbit = inputCheck(nodenum, nodeele, newdata)

    while not cbit:
        nodenum = nodeNum()
        nodeele, newdata = nodeEle(nodenum)   
        cbit = inputCheck(nodenum, nodeele, newdata)

    for l in range(nodenum+1):
        if l == 0:
            objname = 'obj'
            objname += str(l)
            objname = Node(nodeele[l])
            l1 = Sllist(objname)
        else:
            if l < len(nodeele):
                objname = 'obj'
                objname = objname + str(l)
                objname = Node(nodeele[l])
                l1.insertEnd(objname)
        if l == len(nodeele):
            objname = "obj"
            objname = objname + str (l)
            objname = Node(newdata[0])
            l1.insertBeforeNode(objname, newdata[1]) 
    return l1
 
def inputCheck(nodenum, nodeele, newdata):
    cbit = 1
    if nodenum < 1 or nodenum > 1000:
        cbit = 0
    elif cbit:
        for l in range(len(nodeele)):
            if nodeele[l] < 1 or nodeele[l] > 1000:
                cbit = 0
                break
        if newdata[0] < 1 or newdata[0] > 1000:
            cbit = 0
    else:
        if newdata[1] < 0 or newdata[1] > nodenum:
            cbit = 0
    return cbit


l1 = listIni()
l1.printList()

'''
a1 = Node(20)
a2 = Node(30)
a3 = Node(40)
a4 = Node(50)
l1 = Sllist(a1)
l1.insertEnd(a2)
l1.insertEnd(a3)
l1.insertBeforeNode(a4, 2)
l1.printList()
'''