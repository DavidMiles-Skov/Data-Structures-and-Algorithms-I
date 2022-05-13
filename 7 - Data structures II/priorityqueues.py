from math import floor
from re import L

class PriorityQueue:
    
    def __init__(self, array=[]):
        self.array = [None]+array
    
    def bubbleUp(self, x, idx_x):
        parent = self.array[floor(idx_x/2)]
        if parent!=None:
            if parent < x:
                # swapping x and parent
                idx_parent = floor(idx_x/2)
                self.array[idx_parent]=x
                self.array[idx_x]=parent
                return self.bubbleUp(x, idx_parent)
            else:
                return self.array
        else:
            return self.array
        
    def bubbleDown(self,x,idx_x):
        idx_l = idx_x*2
        idx_r = idx_x*2+1
        # Checking if right out of bounds
        if idx_r > len(self.array)-1:
            # check if left is out of bounds
            if idx_l>len(self.array)-1:
                return self.array
            # left is not out of bounds
            else:
                left = self.array[idx_l]
                # if left is greater than x, swap left and x and terminate
                if left>x:
                    self.array[idx_x]=left
                    self.array[idx_l]=x
                return self.array
        # right is not out of bounds
        else:
            # check if smaller than left or right
            left = self.array[idx_l]
            right = self.array[idx_r]
            if left > x or right > x:
                m = max([left, right])
                if m==left:
                    #swap left with x
                    self.array[idx_x]=left
                    self.array[idx_l]=x
                    self.bubbleDown(x, idx_l)
                if m==right:
                    #swap right with x
                    self.array[idx_x]=right
                    self.array[idx_r]=x
                    self.bubbleDown(x, idx_r)

    def max(self):
        return self.array[1]
    
    def insert(self,x):
        self.array.append(x)
        self.array = self.bubbleUp(x,len(self.array)-1)
    
    def extractMax(self):
        if len(self.array)==1:
            return 
        elif len(self.array)==2:
            x=self.array[1]
            self.array=[None]
            return x
        else:
            x = self.array[1]
            self.array=[None]+self.array[2::]
            self.bubbleDown(self.array[1],1)
            return x
    def __str__(self):
        if self.array==[None]:
            return ""
        else:
            s = ""
            for i in self.array[1::]:
                s+=str(i)+" "
        return s
    def __repr__(self):
        return self.__str__()


def main():
    p = PriorityQueue()
    N = int(input())
    for i in range(N):
        s = input()
        if s.split()[0]=="I":
            p.insert(int(s.split()[1]))
        if s=="P":
            print(p)
        if s=="E":
            print(p.extractMax())

main()
    