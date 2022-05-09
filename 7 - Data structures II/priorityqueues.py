class Node:
    def __init__(self,i, difficulty):
        self.i = i
        self.difficulty = difficulty
    def set_next(self, next):
        self.next = next
    
    def get_next(self):
        return self.next
    
    def get_diff(self):
        return self.difficulty

class TaskDelegation:
    
    def __init__(self,n):
        self.top = n
    
    def new_task(self,n):
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

