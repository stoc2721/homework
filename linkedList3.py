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
    def removeDuplicate(self):
        prev = None
        temp = self.head
        data = dict()
        while temp != None:
            if temp.data not in data:
                data[temp.data]=1
                prev = temp
                temp = temp.next
            else:
                prev.next = temp.next
                temp = None
            temp = prev.next
    def print_spot_from_last(self,n):
        distance = self.length() - 1
        temp = self.head
        while temp != None:
            if distance == n-1:
                print(temp.data)
                return
            else:
               distance -=1
               temp = temp.next
    def occurences(self,i):
        count = 0
        temp = self.head
        while temp != None:
            if temp.data == i:
                count = count +1
                temp = temp.next
            else:
                temp = temp.next
        return count
    def rotate(self,k):
        p=self.head
        q=self.head
        prev = None
        count = 0
        while p!= None and count <k:
            prev = p
            p = p.next
            count = count +1
        p = prev
        count = 0
        while q!= None:
            prev = q
            q = q.next
        q = prev
        
        q.next = self.head
        self.head = p.next
        p.next = None
        
    def tail_to_head(self):
        last = self.head
        prev = None
        while last.next != None:
            prev = last
            last = last.next
        last.next = self.head
        self.head=last
        prev.next = None
            
        
            
    
    
lst = linkedList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(1)
lst.printList()
lst.removeDuplicate()
lst.printList()
lst.print_spot_from_last(3)
lst.append(1)
lst.append(1)
lst.append(1)
lst.append(1)
lst.printList()
print(lst.occurences(1),"\n ----")
lst.removeDuplicate()
lst.printList()
lst.rotate(2)
lst.printList()
lst.tail_to_head()
lst.printList()

