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
        if current == None:
            print("----")
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
    def deleteData(self,i):
        temp = self.head
        if temp.data == i:
            self.head=temp.next
            temp=None
        else:
            prev = None
            while temp.data != None and temp.data != i:
                prev = temp
                temp = temp.next
            if temp == None:
                print("There is no data here")
                return
            prev.next = temp.next
            temp = None
    def deleteNode(self,pos):
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        else:
            count = 0
            prev = None
            while temp != None and count != pos:
                prev = temp
                temp=temp.next
                count = count+1
            if temp == None:
                print("Dang, maybe you went too far")
                return
            else:
                prev.next = temp.next
                temp = None
    def length(self):
        count = 0
        temp = self.head
        while temp!= None:
            temp = temp.next
            count = count + 1
        return count
        
    def switch(self,i,j):           # Why move the nodes themselves and not just the data in the nodes?
        if i == j:
            print("These nodes are the same... what's the point of swapping them")
            return
        prev1 = None
        temp1 = self.head
        while temp1 != None and temp1.data != i:
            prev1 = temp1
            temp1=temp1.next
        prev2 = None
        temp2 = self.head
        while temp2 != None and temp2.data != j:
            prev2 = temp2
            temp2 = temp2.next            
        if temp1 == None or  temp2 == None:
            print("This data doesn't exist")
            return
        else:
            if prev1 == None:
                self.head = temp2
                prev2.next = temp1
            elif prev2 == None:
                self.head = temp1
                prev1.next = temp2
            else:
                prev1.next = temp2
                prev2.next = temp1
            fill1 = temp1.next
            fill2 = temp2.next
            temp1.next = fill2
            temp2.next = fill1
    def reverse(self):
        prev = None
        temp = self.head
        while temp != None:
            nxt_temp = temp.next
            temp.next = prev
            prev = temp
            temp=nxt_temp
        self.head=prev
    
    
lst = linkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.printList()
lst.deleteNode(0)
lst.printList()
lst.prepend(1)
lst.printList()
print(lst.length(),"\n ----")
lst.switch(2,3)
lst.printList()
lst.reverse()
lst.printList()
