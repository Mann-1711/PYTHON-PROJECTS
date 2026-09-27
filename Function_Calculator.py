# A calculator made by using function:
ans=input(("what do you user wanna do:[calculation=1 or exit=2 ]:"))
if(ans=="1"):
 num1=float(input("enter the 1st number:"))
 num2=float(input("enter the 2nd number:"))
 operator=input("choose the operator to be performed[+,-,*,%]:")
 def oper(num1,num2,operator):
    if(operator=="+"):
        print("ans:",num1+num2)
    elif(operator=="-"):
        print("ans:",num1-num2)
    elif(operator=="*"):
        print("ans:",num1*num2)
    elif(operator=="%"):
        print("ans:",num1%num2)
    else:
        print("invalid operator")
elif(ans=="2"):
    print("you have exited calculator")
