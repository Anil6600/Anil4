# -*- coding: utf-8 -*-
"""Copy of Untitled38.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sgGTB1qPCg1E2amHuYcMwyAak06EoP3l
"""

a= input("Enter input :" )
try:
   inp= int(a)
   if(a==str(a)[::-1]):
      print('PALINDROME')
   else:
      print('NOT a palindrome')
except ValueError:
   print("That's not a valid number, Try Again !")
finally:
    print("statement executed")

a= input("Enter input :" )
try:
   inp= int(a)
   if(a==str(a)[::-1]):
      print('PALINDROME')
   else:
      print('NOT a palindrome')
except ValueError:
   print("That's not a valid number, Try Again !")
finally:
    print("statement executed")