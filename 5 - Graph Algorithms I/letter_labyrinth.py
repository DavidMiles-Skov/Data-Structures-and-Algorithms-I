class Node:
    def __init__(self,x, y):
        self.x=x
        self.y=y
        self.adj = []
    def set_down(self,n):
        self.adj.append(n)
    def set_up(self,n):
        self.adj.append(n)
    def set_right(self,n):
        self.adj.append(n)
    def set_left(self,n):
        self.adj.append(n)


