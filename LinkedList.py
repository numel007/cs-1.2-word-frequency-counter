from Node import Node

class LinkedList:

  def __init__(self):
    self.head = None


  def append(self, new_data):
    # Instantiate new Node object, set next pointer of the object to point at previous head, and set object as the head of the LL
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node


  def find(self,item):

    # Start at the head/first object of the LL
    current = self.head

    found = False
    counter = 0

    # Loop for as long as there are still items to search in the LL or the item has not been found
    while current != None and not found:

      # Set found to true if ite is located
      if current.data == item:
        found = True
      # Search the next LL item and increase counter
      else:
        current = current.next
        counter += 1

    # When item is found or no items remain
    if found:
      return counter
    else:
      return -1



  def length(self):
    if self.head == None:
      return 0
    else:
      counter = 1
      current = self.head
      while(current.next):
        current = current.next
        counter +=1
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'Node {i}: {current.data}')
        current = current.next