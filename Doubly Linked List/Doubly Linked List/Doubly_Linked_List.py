
#Task -- Doubly linked list using a single key (data)
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None 

class Dllist():
    def __init__(self,head=None):
        self.head = head
#        self.first = None
        self.last = None

    def printList(self):
        link = self.head
        while link != None:
            print(link.data, end=" ")
            link = link.next
        print("")

    def insertBegin(self, node):
        link = self.head
        if link == None:
            self.head = node
        else:
            self.last = node
            node.next = link
            link.prev = node
            self.head = node

    def insertEnd(self, node):
        link = self.head
        if link == None:
            self.head = node
        else:
            while link.next != None:
                link = link.next
            link.next = node
            node.prev = link

    def insertAfterNode(self, node, data):
        link = self.head
        if link == None:
            self.head = link

        while link.data != data:
            link = link.next

        node.next = link.next
        link.next = node
        node.prev = link 

    def insertBeforeNode(self, node, data):
        link = self.head
        if link == None:
            self.head = link

        while link.data != data:
            prev = link
            link = link.next
        node.next = prev.next
        prev.next = node
        node.next = link
        link.prev = node

    def insertInNode(self, node, data, data1):
        link = self.head 
        if link == None:
            self.head = node
        
        while link.data != data:
            prev = link
            link = link.next
        prev = link
        link = link.next
        prev.next = node.next
        prev.next = node
        node.next = link
        link.prev = node

    def deleteBegin(self):
        link = self.head
        if link == None:
            return
        else:
            self.head = link.next

    def deleteEnd(self):
        link = self.head
        if link == None:
            return
        else:
            while link.next.next != None:
                link = link.next
        link.next = None

    def deleteBeforeNode(self, data):
        link = self.head 
        if link == None:
            return
        else:
            while link.next.next.data != data:
                prev = link
                link = link.next
            prev = link
            link = link.next
            prev.next = link.next

    def deleteAfterNode(self, data):
        link = self.head
        if link == None:
            return  
        else:
            while link.data != data:
                prev = link
                link = link.next
            prev = link
            link = link.next
            prev.next = link.next

    def reverseList(self):
        link = self.head
        if link == None:
            return
        else:
            temp = None
            prev = None
            while link.next != None:
                temp = link.next
                link.next = prev
                prev = link
                prev.prev = temp
                link = temp
            link.next = prev
            self.head = link


a1 = Node(10)
dl1 = Dllist(a1)

a2 = Node(20)
dl1.insertBegin(a2)

a3 = Node(30)
dl1.insertEnd(a3)

a5 = Node(50)
dl1.insertAfterNode(a5, 10)

a6 = Node(60)
dl1.insertBeforeNode(a6, 50)

a7 = Node(70)
dl1.insertInNode(a7, 60, 50)
dl1.deleteBegin()
dl1.deleteEnd()
#dl1.deleteBeforeNode(50)
#dl1.deleteAfterNode(10)
dl1.reverseList()

dl1.printList()