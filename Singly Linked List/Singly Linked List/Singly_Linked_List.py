#Task -- Create a singly linked list with insert, delete & print functions

##Singly linked list Node
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None


##Singly linked list with print & variant insert and delete functions
class Llist(Node):
    def __init__(self, head=None):
        self.head = head

#Prints linkedlist data elements
    def printList(self):
        link = self.head
        while link != None:
            print(link.data, end=" ")
            link = link.next
        print("")

#Inserts node at the beginning of the linkedlist
    def insertBegin(self, node):
        link = self.head
        if link == None:
            self.head = node
        else:            
            node.next = link
            self.head = node

#Inserts node at the end of the linkedlist
    def insertEnd(self, node):
        link = self.head
        if link == Node:
            self.head = node
        else:
            while link.next != None:
                link = link.next
            link.next = node

#Inserts node before a given node
    def insertBeforeNode(self, node, data):
        link = self.head
        while link.data != data:
            prev = link
            link = link.next
        node.next = link
        prev.next = node

#Inserts node after a given node  
    def insertAfterNode(self, node, data):
        link = self.head
        while link.data != data:
            link = link.next
        node.next = link.next
        link.next = node

#Deletes node at the beginning of the linkedlist
    def deleteBegin(self):
        link = self.head
        if link == None:
            pass
        else:
            self.head = link.next

#Deletes node at the end of the linkedlist
    def deleteEnd(self):
        link = self.head
        while link.next.next != None:
            link = link.next
        link.next = None

#Deletes node after a given node    
    def deleteAfterNode(self,data):
        link = self.head
        prev = None
        while link.data != data:
#            prev = link
            link = link.next
        prev = link
        link = link.next
        prev.next = link.next

#Deletes node before at a given node   
    def deleteBeforeNode(self,data):
        link = self.head
        prev = None
        while link.next.next.data != data:
            prev = link
            link = link.next
        prev = link
        link = link.next
        prev.next = link.next

#Reverses a linkedlist   
    def reverseList(self):
        link = self.head
        prev = None 
        temp = None
        while link.next != None:
            temp = link.next
            link.next = prev
            prev = link
            link = temp
        link.next = prev
        self.head = link

###############################################################################################
######## Main Code Block ######################################################################

a1 = Node(20)
l1 = Llist(a1)
a2 = Node(30)
a3 = Node(40)
a4 = Node(10)
a5 = Node(50)

l1.insertBegin(a2)
l1.insertBegin(a3)
l1.insertEnd(a4)
l1.insertEnd(a5)
l1.deleteBegin()
#l1.deleteEnd()
l1.deleteAfterNode(20)
l1.deleteBeforeNode(50)
a6 = Node(20)
l1.insertBeforeNode(a6,50)
a10 = Node(90)
l1.insertAfterNode(a10,50)
l1.reverseList()
l1.printList()

#l1.insertBegin(a3)
#a1.next = a2
#a2.next = a3