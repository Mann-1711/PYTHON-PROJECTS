# Student Marks Calculator:
dec=input("Do you wanna use student marks calculator:").lower()
if(dec=="yes"):
 eng=float(input("enter marks in english:"))
 math=float(input("enter marks in maths:"))
 sci=float(input("enter marks in science:"))
# Function to calculate total:
 def total(n1,n2,n3):
    print("total:",n1+n2+n3)
#Function to Calculate percentage:
 def percentage(n1,n2,n3):
    print("percentage:", (n1+n2+n3)/300*100)
# Function to Find highest marks:
 def highest(n1,n2,n3):
    if(n1>n2 and n1>n3 ):
        print("highest marks:",n1)
    elif(n2>n1 and n2>n3 ):
        print("highest marks:",n2)
    elif(n3>n1 and n3>n2 ):
        print("highest marks:",n3)
# Function to Find lowest mark:
 def lowest(n1,n2,n3):
    if(n1<n2 and n1<n3 ):
        print("lowest marks:",n1)
    if(n2<n1 and n2<n3 ):
        print("lowest marks:",n2)
    if(n3<n2 and n3<n1):
        print("lowestr marks:",n3)
#function to Decide pass/fail:
 def pass_fail(n1,n2,n3):
    per=(n1+n2+n3)/300*100
    if(per<33.0):
        print("FAIL")
    else:
        print("PASS")
 total(eng,math,sci)
 percentage(eng,math,sci)
 highest(eng,math,sci)
 lowest(eng,math,sci)
 pass_fail(eng,math,sci)
