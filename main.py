#!/usr/bin/env python
import random as rd
import string as st
import sys

def passlen():
  if len(sys.argv)>1:
    try:
      lp = int(sys.argv[1])
      if 8<=lp<=16:
        return lp
      else:
        print('please enter a number between 8-16')
        return None
    except ValueError:
      print('please enter a valid number')
      return None
  return None

lp = passlen()
if lp is None:
  while True:
    try:
      lp = int(input('enter your password length (8-16): '))
      if 8<=lp<=16:
        break
      else:
        print('please enter a number between 8-16')
    except ValueError:
      print('please enter a valid number')
      sys.exit()

data = [
  list(st.ascii_uppercase),
  list(st.ascii_lowercase),
  list(st.digits),
  list(st.punctuation)
]

md = sum(data,[])
box = []
for i in range(lp):
  box.append(rd.choice(md))
  
result = ''.join(box)
print(f'Your Password: {result}')