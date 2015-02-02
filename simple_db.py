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
    self.update_log = []
    self.value_counts = Counter()

  # TODO
  def set(self, name, val):
    print 'User has chosen to SET var ', name, ' to: ', val

  # TODO
  def get(self, name):
    print 'User has chosen to GET var ', name

  # TODO
  def unset(self, name):
    print 'User has chosen to UNSET var ', name

  # TODO
  def get_num_equal_to(self, val):
    print 'User has chosen to find NUMEQUALTO ', val

  # TODO
  def start_transaction(self):
    print 'User chose to begin a new transaction block, so there are now '

  # TODO
  def rollback(self):
    print 'User chose to rollback to previous transaction block'
  
  # TODO
  def commit(self):
    print 'User chose to commit current transaction block'

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
  