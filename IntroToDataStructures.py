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
    

# 
