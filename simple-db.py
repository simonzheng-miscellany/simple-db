# By: Simon Zheng (github.com/simonzheng)
# 20150128

import sys

if __name__ == '__main__':
  while True:
    sys.stdout.write('> ')
    input_arr = sys.stdin.readline().strip().split(' ')

    cmd = input_arr[0]
    # TODO: error check for extra args?

    # Data commands
    if cmd == 'SET' and len(input_arr) == 3:
      name = input_arr[1]
      val = input_arr[2]
      print 'User has chosen to SET var ', name, ' to: ', val
    elif cmd == 'GET' and len(input_arr) == 2:
      name = input_arr[1]
      print 'User has chosen to GET var ', name
    elif cmd == 'UNSET' and len(input_arr) == 2:
      name = input_arr[1]
      print 'User has chosen to UNSET var ', name
    elif cmd == 'NUMEQUALTO' and len(input_arr) == 2:
      val = input_arr[1]
      print 'User has chosen to find NUMEQUALTO ', val
    elif cmd == 'END' and len(input_arr) == 1:
      print 'User has chosen to exit.'
      break
    # Transaction Commands
    elif cmd == 'BEGIN' and len(input_arr) == 1:
      print 'User chose to begin a new transaction block'
    elif cmd == 'ROLLBACK' and len(input_arr) == 1:
      print 'User chose to rollback to previous transaction block'
    elif cmd == 'COMMIT' and len(input_arr) == 1: 
      print 'User chose to commit current transaction block'
    else:
      print 'Invalid command or number of arguments.'
      print 'See valid commands at: http://www.thumbtack.com/challenges/simple-database'
    print input_arr
    print
  
