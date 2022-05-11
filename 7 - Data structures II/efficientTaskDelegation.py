class Node:
  def __init__(self, ID, difficulty):
    self.difficulty = difficulty
    self.ID=ID
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def addTask(self, n):
    curr = self.head
    if curr is None:
      self.head = n
      return

    if curr.difficulty < n.difficulty:
      n.next = curr
      self.head = n
      return

    while curr.next is not None:
      if curr.next.difficulty < n.difficulty:
        break
      curr = curr.next
    n.next = curr.next
    curr.next = n
    return
  
  def requestTask(self):
    r = self.head
    new_head = self.head.next
    self.head=new_head
    return r



# Handling codejudge input
T = LinkedList()
N = int(input())
for i in range(N):
    s = input()
    if s.split()[0]=='N':
        i=int(s.split()[1])
        d = int(s.split()[2])
        T.addTask(Node(i,d))
    else:
        n = T.requestTask()
        print(n.ID)
