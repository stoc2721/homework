class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            return
        else:
            last = self.head
            while last.next != None:
                last = last.next
            last.next = temp
    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
    def prepend(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            temp.next =self.head
            self.head = temp
    def insertAfterNode(self,prevNode,data):
        temp = Node(data)
        temp.next=prevNode.next
        prevNode.next=temp
    def delete(self,i):
        temp = self.head
        if temp.data == i:
            self.head=temp.next
            temp.next=None
        else:
            prev = None
            while temp.data != i:
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp.next = None
        
        
        
lst = linkedList()
lst.append(1)
lst.append(2)
lst.printList()
lst.prepend(3)
lst.printList()
lst.insertAfterNode(lst.head.next.next,4)
lst.printList()
lst.delete(2)
lst.printList()
