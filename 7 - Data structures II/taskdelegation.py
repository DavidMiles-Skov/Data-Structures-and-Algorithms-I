class Node:
    def __init__(self,i, difficulty):
        self.i = i
        self.difficulty = difficulty
        self.next=None
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def get_diff(self):
        return self.difficulty


class TaskDelegation:
    
    def __init__(self,n=None):
        self.top = n
    
    def new_task(self,n):
        if self.top==None:
            self.top = n
        elif n.get_diff() > self.top.get_diff():
            n.set_next(self.top)
            self.top = n
        else:
            curr_node = self.top
            prev_node = None
            while curr_node.get_diff()>n.get_diff():
                prev_node = curr_node
                if curr_node.get_next() == None:
                    curr_node.set_next(n)
                    return
                else:
                    curr_node = curr_node.get_next()
            prev_node.set_next(n)
            n.set_next(curr_node)
    
    def request_task(self):
        r = self.top
        self.top = self.top.get_next()
        return r

# Handling codejudge input
T = TaskDelegation()
N = int(input())
for i in range(N):
    s = input()
    if s.split()[0]=='N':
        i=int(s.split()[1])
        d = int(s.split()[2])
        T.new_task(Node(i,d))
    else:
        n = T.request_task()
        print(n.i)
