class Node:
    def __init__(self, num, next=None):
        self.val = num
        self.next = next
    def setNext(self,node):
        self.next = node
    def getNext(self):
        return self.next

class StackUsingLinkedList:
    def __init__(self, initial_node=None):
        if initial_node==None:
            self.top=None
        else:
            self.top=initial_node
    def PUSH(self,n):
        if self.top!=None:
            new_top = n
            prev_top = self.top
            self.top = new_top
            new_top.setNext(prev_top)
        else:
            self.top = n
    def POP(self):
        print(self.top.val)
        self.top = self.top.getNext()
        

N = int(input())
S = StackUsingLinkedList()

for i in range(N):
    s=input()
    if s=="PO":
        S.POP()
    else:
        num = int(s.split()[1])
        S.PUSH(Node(num))