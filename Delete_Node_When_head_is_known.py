# Writing the necessary functions

# Linked List Class
class LLNode:
  def __init__(self,data):
    self.data = data
    self.next = None

# Function to get the input of the elements of the LL
def GetInput():
  # storing the input as a list
  Inp_list = [int(elem) for elem in input().split()]

  head = None
  tail = None

  for num in Inp_list:
    # -1 indicates that it is the end of the list
    if num==-1:
      break
    # creating a LL node
    Node = LLNode(num)

    # creating the LL
    if head==None:
      head = Node
      tail = Node
    else:
      tail.next = Node
      tail = Node

  return head

# Function to obtain the length of the LL
def GetLL_Length(head):
  temp = head
  count = 1
  while temp.next!=None:
    temp = temp.next
    count+=1
  return count

# Function to print the LL
def PrintLL(head):
  temp = head
  while temp!=None:
    print(f'{temp.data}-->',end='')
    temp = temp.next
  print('None')

# THE FOLLOWING IS THE Function to delete the given node in the LL
def DeleteNode(head,node):
  curr = head
  prev = None
  count = 0
  while curr.data!=node:
    prev = curr
    curr = curr.next
    count+=1

  if count==0:
    head = head.next
    curr.next = None
  else:
    prev.next = curr.next
    curr.next = None

  return head
