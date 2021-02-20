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
      arr.append(new_ll)

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

    # Traverse the linkedlist at key_hash in array, and search for the key
    # If the same key is found, read the associated value and increment by 1
    new_tuple_to_insert = self.arr[key_hash].find_and_update(key)

    if new_tuple_to_insert == -1:
      self.arr[key_hash].append(item)


  def print_key_values(self):
    
    for linkedlist in self.arr:
      linkedlist.print_nodes()
      print('Moving to next linkedlist')
    print('---Print complete---')