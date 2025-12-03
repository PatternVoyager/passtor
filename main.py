#!/usr/bin/env python
from datetime import datetime as dt
import random as rd
import string as st
import sys
import os

def passlen():  # get password length from command line argument
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

def save_pass_arg(result):  # save password from command line argument
  if len(sys.argv)>2:
    try:
      save = sys.argv[2].strip().lower()
      if save == 'y':
        in_save = 'y'
        return save
      elif save == 'n':
        in_save = 'n'
        return save
      else:
        print('Invalid input for saving password.')
        return None
    except:
      pass

def save_password(result):  # save password to csv file with date and time
  sv = save_pass_arg(result)
  if sv is not None:
    in_save = sv
  else:
    in_save = input('Do you want to save the password? (y/n): ').strip().lower()
  
  date = dt.now().strftime('%Y-%m-%d')
  time = dt.now().strftime('%H:%M:%S')

  csv = {
    'created_at': date,
    'time': time,
    'password': result,
    'length': len(result)
  }

  if in_save == 'y':
    file_exists = False
    try:
      with open('passwords.csv', 'r') as f:
        file_exists = True
    except:
      file_exists = False

    columns = ['created_at', 'time', 'password', 'length']
    file_exists = os.path.isfile('passwords.csv')
    with open('passwords.csv', 'a') as f:
      if not file_exists:
        
        f.write(columns[0] + ',' + columns[1] + ',' + columns[2] + ',' + columns[3] + '\n')
      f.write(f"{csv['created_at']},{csv['time']},{csv['password']},{csv['length']}\n")
    print('Password saved to passwords.csv')
  elif in_save == 'n':
    pass
  else:
      print('Invalid input, Password not saved.')

def main(): # main function to generate password
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
    list(st.punctuation.replace(',',''))  # exclude comma to avoid csv issues
  ]

  md = sum(data,[])
  box = []
  for i in range(lp):
    box.append(rd.choice(md))
    
  result = ''.join(box)
  print(f'Your Password: {result}')
  save_password(result)

if __name__ == '__main__':
  main()

