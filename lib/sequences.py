#!/usr/bin/env python3

def print_fibonacci(length):
  x = []
  if length == 0:
      x = [0,1]
      print(x)
  elif length == 1:
      x = [0,1]
      print(x)
  else: 
      x = [0,1]
  for i in range(2,length):
        x.append(x[i-1] + x[i-2])
  print(x)

        