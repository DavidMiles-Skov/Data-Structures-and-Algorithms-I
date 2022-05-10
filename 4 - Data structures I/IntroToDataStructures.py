# 1.4 - Implementing a Queue with 2 stacks 

class Stack:
    def __init__(self, n, arr=[]):
        self.size = n
        self.push_idx = 0
        if arr==[]: self.array = [None for i in n]
        else: self.array = arr
    def push(self,val):
        if self.push_idx <= self.size-1:
            self.array[self.push_idx] = val
            self.push_idx+=1
        else:
            print("Exceeded stack size.")
    def pop(self):
        if self.push_idx == self.size:
            ret_val = self.array[-1]
            self.array[-1] = None
            return ret_val
        else:
            ret_val = self.array[self.size-1]
            self.array[self.size-1] = None
            self.push_idx-=1
            return ret_val

def reverse_stack(s):
    return Stack(s.size, s.array[-1::-1])

class QueueWithStacks:
    def __init__(self, n):
        self.InStack = Stack(n)
        self.OutStack = Stack(n)
    def updateOutStack(self):
        self.OutStack.array = self.InStack.array[-1::-1]
    def updateInStack(self):
        self.InStack.array = self.OutStack.array[-1::-1]
    def ENQUEUE(self,val):
        self.InStack.push(val)
        self.updateOutStack() # O(n)
    def DEQUEUE(self):
        ret_val = self.OutStack.pop()
        self.updateInStack() # O(n)
        return ret_val
    

# 5.1 - Stack containing integers using singly-linked list

class Node:
    def __init__(self, num, next=None):
        self.val = num
        self.next = next
    def setNext(self,node):
        self.next = node
    def getNext(self):
        return self.next
    def getVal(self):
        return self.val

class StackUsingLinkedList:
    def __init__(self, initial_node=None):
        self.base = Node(None)
        self.base.setNext(initial_node)
        self.top = initial_node
    def PUSH(self,val):
        new_top = Node(val)
        self.top = new_top
    def POP(self):
        curr_node = self.base
        nxt_node = self.base.getNext()
        if nxt_node == None:
            print("Empty Stack. Unable to POP.")
            return None
        else:
            while nxt_node.getNext() != None:
                curr_node = nxt_node
                nxt_node = curr_node.getNext()
            curr_node.setNext(None)
            self.top = curr_node
            return nxt_node

# 5.2 - Queue using linked list

class QueueUsingLinkedList:
    def __init__(self, firstnode=None):
        self.frontNode = firstnode
        self.base = Node(None)
    def ENQUEUE(self, node):
        # If Queue is empty
        if self.base.getNext() is None:
            self.base.setNext(node)
            self.frontNode = node
        # If Queue is not empty
        else:
            prev_last = self.base.getNext()
            self.base.setNext(node)
            node.setNext(prev_last)
    def DEQUEUE(self):
        curr_node = self.base
        nxt_node = self.base.getNext()
        if nxt_node == None:
            print("Empty Queue. Unable to DEQUEUE.")
            return None
        else:
            while nxt_node.getNext() != None:
                curr_node = nxt_node
                nxt_node = curr_node.getNext()
            curr_node.setNext(None)
            self.top = curr_node
            return nxt_node

        
# 9.1 - Stacks using dynamic arrays 

class DynamicStack:
    def __init__(self):
        self.array = []
    def PUSH(self,x): # O(1)
        self.array=[x]+self.array
    def POP(self):
        ret_val = self.array[0] 
        self.array.remove(0) # O(1)
        return ret_val


    


        
