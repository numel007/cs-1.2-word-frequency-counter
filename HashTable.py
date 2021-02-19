from LinkedList import LinkedList

class HashTable:

  def __init__(self, size):
    self.size = size
    self.arr = self.create_arr(size)


  def create_arr(self, size):
    '''Create array of linkedlists'''
    arr = []

    for i in range(size):
      new_ll = LinkedList()
      arr.append(mew_ll)

    return arr


  def hash_func(self, key):
    
    # First, get the first letter of the key and cast to lowercase
    first_letter = key[0].lower()

    # Calculate distance of first_letter from a
    distance = ord(first_letter) - ord('a')

    # Index is determined by the remainder of (distance/array_size)
    index = distance % self.size

    # Return index of input
    return index


  def insert(self, key, value):
    
    # First, determine the index to insert key and value at
    # Key, in this case, is the word from the text fle
    key_hash = self.hash_func(key) 

    # Create a tuple of the key and value
    item = (key, value)

    # Insert tuple into selected linkedlist
    self.arr[key_hash].append(item)




  # 4️⃣ TODO: Complete the print_key_values method.

  # Traverse through the every Linked List in the table and print the key value pairs.

  # For example: 
  # a: 1
  # again: 1
  # and: 1
  # blooms: 1
  # erase: 2

  def print_key_values(self):
    
    for linkedlist in self.arr:
      linkedlist.print_nodes()
      print('Moving to next linkedlist')
    print('---Print complete---')