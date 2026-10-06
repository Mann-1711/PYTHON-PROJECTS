# This is a program to create a unit convertor using basic functions:
a=input("Do you wanna use unit convertor:").lower()
if(a=="yes"):
 uni=float(input("Input the total number you wanna convert:"))
 conv=input("In which of these units do you wanna convert the value[km → miles,miles → km,°C → °F,°F → °C,kg → pounds] :").lower()
 if(conv=="km to miles"):
  def km_m(num):
      print(num*0.621371)
  km_m(uni)

 if(conv=="miles to km"):
   def m_km(num):
      print(num*1.60934)
   m_km(uni)

 if(conv=="cel to feh"):
  def c_f(num):
      print((num*9/5) + 32)
  c_f(uni)

 if(conv=="feh to cel"):
  def f_h(num):
      print((num-32)*5/9)
  f_h(uni)
 if(conv=="kg to pound"):
   def kf_p(num):
      print(num*2.20462)
   kf_p(uni)

 