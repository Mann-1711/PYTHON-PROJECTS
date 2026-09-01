#calculator
num1=float(input("ENTER ANY NUMBER:"))
num2=float(input("ENTER OTHER NUMBER:"))
opr=input("ENTER THE OPERATION YOU WANNA PERFORM[+,-,*,%]:")
if(opr=="+"):
    print("answer:",num1+num2)
elif(opr=="-"):
    print("answer:",num1-num2)
elif(opr=="*"):
    print("answer:",num1*num2)
elif(opr=="%"):
    print("answer:",num1%num2)
else:
    print("INVALID OPERATION")
