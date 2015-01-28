# By: Simon Zheng (github.com/simonzheng)
# 20150128

import sys

if __name__ == '__main__':
  while True:
    sys.stdout.write('> ')
    line = sys.stdin.readline().strip().split(' ')
    print line