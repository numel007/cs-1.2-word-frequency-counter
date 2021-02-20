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

    current = self.head

    found = False
    counter = 0

    while current != None and not found:

      if current.data[0] == item:
        found = True
        return current.data
      else:
        current = current.next
        counter += 1

    if found:
      pass
    else:
      return -1

  def find_and_update(self,item):

    # Start at the head/first object of the LL
    current = self.head

    found = False

    # Loop for as long as there are still items to search in the LL or the item has not been found
    while current != None and not found:

      # Set found to true if ite is located
      if current.data[0] == item:
        found = True
      # Search the next LL item
      else:
        current = current.next

    # When item is found or no items remain
    if found:
      # Update current to an incremented value
      value = current.data[1]
      new_tuple = (current.data[0], (value + 1))
      current.data = new_tuple
    else:
      return -1


  def length(self):

    # Immediately return 0 if no object at head
    if self.head == None:
      return 0
    # Set current to the first object in LL, instantiate counter at 1
    else:
      counter = 1
      current = self.head

      # While current.next is True, traverse the LL and increment counter
      while(current.next):
        current = current.next
        counter +=1

      # When current.next evaluates False, return counter
      return counter


  def print_nodes(self):
    current = self.head
    
    if current == None:
      print('The linked list is empty.')
    else:
      for i in range(self.length()):
        print(f'Node {i}: {current.data}')
        current = current.next