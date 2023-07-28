
#Task -- Create a  Doubly linked list with a single key (data)


#A doubly linkedlist Node
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        self.prev = None 


#Doubly linkedlist structure with various functions
class Dllist():
    def __init__(self,head=None):
        self.head = head
#        self.first = None
        self.last = None

#Prints data in a linkedlist structure
    def printList(self):
        link = self.head
        while link != None:
            print(link.data, end=" ")
            link = link.next
        print("")

#Inserts a node at the beginning of a node
    def insertBegin(self, node):
        link = self.head
        if link == None:
            self.head = node
        else:
            self.last = node
            node.next = link
            link.prev = node
            self.head = node

#Inserts a node at the end of a linkedlist
    def insertEnd(self, node):
        link = self.head
        if link == None:
            self.head = node
        else:
            while link.next != None:
                link = link.next
            link.next = node
            node.prev = link

 #Inserts a node after a given node
    def insertAfterNode(self, node, data):
        link = self.head
        if link == None:
            self.head = link

        while link.data != data:
            link = link.next

        node.next = link.next
        link.next = node
        node.prev = link 

#Inserts a node before a given node
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

 #Inserts a node between two nodes 
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

#Deletes a node at the beginning
    def deleteBegin(self):
        link = self.head
        if link == None:
            return
        else:
            self.head = link.next

#Deletes a node at the end of a linkedlist
    def deleteEnd(self):
        link = self.head
        if link == None:
            return
        else:
            while link.next.next != None:
                link = link.next
        link.next = None

#Deletes a node before a provided key
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


#Deletes a node after a provided key
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

#Reverses linkedlist 
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


################################################################################################################################
############ Main Block of Code ################################################################################################

# A Series of add, insert, delete 7 reverse operations

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