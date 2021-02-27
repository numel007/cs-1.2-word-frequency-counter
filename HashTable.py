from LinkedList import LinkedList
import requests
import json
import math
import os
from dotenv import load_dotenv

load_dotenv()

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

    value = 0
    print(f'Calculating hash for {key}')


    for letter in key:

      # Add letter to value
      value += ord(letter)

      # Request the current stock info
      raw_data = requests.get(os.getenv('API_URL'))
      print(f'Status code: {raw_data}')

      # Handle if the api is down
      if str(raw_data) == '<Response [200]>':
        data = json.loads(raw_data.content)
        print(f"Current price: {data['current']}")
        print(f"Points change: {data['points_change']['points']}")

        # Add current price to value, then divide by absolute val of GME's points up/down.
        # NOTE: This means the resultant value will be changing if the market is open
        # Pretty much, don't attempt to perform a search for a hash unless the hash was created while
        # the market was closed, as well as having the search conducted before the market re-opens.
        value += data['current'] / abs(data['points_change']['points'])
      else:
        print('API is down, skipping value modification')
        break


    # Index is determined by the remainder of (rounded value/array_size)
    index = math.ceil(value) % self.size

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