# This is a program to create a unit convertor using basic functions:
a=input("Do you wanna use unit convertor:")
if(a=="yes"):
 uni=float(input("Input the total number you wanna convert:"))
 conv=input("In which of these units do you wanna convert the value[km → miles,miles → km,°C → °F,°F → °C,kg → pounds] :")
 def km_m(n):
  print(n)