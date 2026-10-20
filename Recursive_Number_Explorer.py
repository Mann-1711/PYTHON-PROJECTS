# Recursive Number Explorer:
n=int(input("Enter any number:"))
action=input("Which action do you wanna perform[Countdown,Recursive sum,Factorial,All]:").lower()
if(action=="countdown" or action=="all"):
# Countdown:
 def rev_count(num):
    if(num==0):
        return
    print("Countdown:",num)
    rev_count(num-1)
 rev_count(n)
if(action=="sum" or action=="all"):
#Recursive sum:
   def sum(n):
      if(n==0):
         return 0
      return n+sum(n-1)
   print("Recursive sum:",sum(n))
if(action=="fact" or action=="all"):
   # Factorial:
   def fact(num):
      if(num==0 or num==1):
         return 1
      else:
         return num*fact(num-1)
   print("Factorial:",fact(n))