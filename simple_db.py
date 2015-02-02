# simple_db.py simulates a simple in-memory DB
# Usage: python simple_db.py
# By: Simon Zheng (github.com/simonzheng)
# 20150128
# Requires: Python 2.7+ since I use the Counter collection object

import sys
from collections import Counter

class SimpleDB:
  def __init__(self):
    self.data = {}
    self.update_log = [] # We use update_log as a Python stack to track all old values that get changed within each transaction block
    self.value_counts = Counter()

  # TODO: test this extensively with unsetting values
  def set(self, name, new_val):
    print 'User has chosen to SET var ', name, ' to: ', new_val
    
    # Get previous value
    old_val = None
    if name in self.data:
      old_val = self.data[name]

    # Set new value
    self.data[name] = new_val

    # Update the update log's most recent transaction block with oldest value of this variable
    if (len(self.update_log) > 0) and (name not in self.update_log[0]): # Assume len is O(1) operation using internal counter and not iterating through all elems
        self.update_log[0][name] = old_val

    # Update value counts
    if old_val != None:
      self.value_counts[old_val] -= 1
    self.value_counts[new_val] += 1

  def get(self, name):
    print 'User has chosen to GET var ', name
    print self.data[name]

  # TODO
  def unset(self, name):
    print 'User has chosen to UNSET var ', name

  def get_num_equal_to(self, val):
    print 'User has chosen to find NUMEQUALTO ', val
    print self.value_counts[val]

  def start_transaction(self):
    self.update_log.append({})
    print 'User chose to begin a new transaction block, so there are now ', len(self.update_log), ' blocks'

  def rollback(self):
    # TODO: For loop through most recent transaction block and reset values that were changed

    self.update_log.pop()
    print 'User chose to rollback to previous transaction block, so there are now ', len(self.update_log), ' blocks'


  def commit(self):
    self.update_log.pop()
    print 'User chose to commit current transaction block, so there are now ', len(self.update_log), ' blocks'

def main():
  db = SimpleDB()

  while True:
    sys.stdout.write('\n> ')
    input_arr = sys.stdin.readline().strip().split(' ')

    cmd = input_arr[0]
    # Data commands
    if cmd == 'SET' and len(input_arr) == 3:
      name = input_arr[1]
      val = input_arr[2]
      db.set(name, val)
    elif cmd == 'GET' and len(input_arr) == 2:
      name = input_arr[1]
      db.get(name)
    elif cmd == 'UNSET' and len(input_arr) == 2:
      name = input_arr[1]
      db.unset(name)
    elif cmd == 'NUMEQUALTO' and len(input_arr) == 2:
      val = input_arr[1]
      db.get_num_equal_to(val)
    elif cmd == 'END' and len(input_arr) == 1:
      print 'User has chosen to exit.'
      break

    # Transaction Commands
    elif cmd == 'BEGIN' and len(input_arr) == 1:
      db.start_transaction()
    elif cmd == 'ROLLBACK' and len(input_arr) == 1:
      db.rollback()
    elif cmd == 'COMMIT' and len(input_arr) == 1: 
      db.commit()
    else:
      print 'ERROR: Invalid command or number of arguments.'
      print 'See valid commands at: http://www.thumbtack.com/challenges/simple-database'
    
    # Print input array
    print input_arr

if __name__ == '__main__':
  main()
  