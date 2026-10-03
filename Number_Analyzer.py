# Number Analyzer:
yn=input("Do you wanna use number analyzer:")
if(yn=="yes"):
 num=int(input("enter any number:"))
 # Function to check odd even:
 def odd_even(n):
  if(num%2==0):
   print("Even number")
  elif(num%2!=0):
   print("Odd number")
#Function Check whether number is positive/negative:
 def pos_neg(n):
  if(num<0):
   print("negative number")
  elif(num>0):
   print("positive number")
# Function to Find its square
 def square(n):
  print("Square:",num*num)
#Function to Find its factorial:
 def fact(n):
  if(n==0):
   return 0
  if(n>0):
   return fact(n-1)+n
 odd_even(num)
 pos_neg(num)
 square(num)
 print(fact(num))
