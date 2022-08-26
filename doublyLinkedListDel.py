class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.start_node = None
    
    def insertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("is empty")

    def insertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
    
    def deleteAtStart(self):
        if self.start_node is None:
            print("no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None;

    def deleteAtEnd(self):
        if self.start_node is None:
            print("no element to delete")
            return 
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None
   
    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")
#Creatng new doublyLinkedList
#performing insertion and deletion
NewDoublyLinkedList = doublyLinkedList()
NewDoublyLinkedList.insertToEmptyList(9)
NewDoublyLinkedList.insertToEnd(8)
NewDoublyLinkedList.insertToEnd(7)
NewDoublyLinkedList.insertToEnd(6)
NewDoublyLinkedList.insertToEnd(5)
NewDoublyLinkedList.insertToEnd(4)
NewDoublyLinkedList.Display()
NewDoublyLinkedList.deleteAtStart()
NewDoublyLinkedList.deleteAtStart()
NewDoublyLinkedList.Display()
NewDoublyLinkedList.deleteAtEnd()