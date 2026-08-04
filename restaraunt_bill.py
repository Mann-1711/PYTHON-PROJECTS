#DISCOOUNT ON RESTARAUNT BILL
bill=float(input("ENTER THE TOTAL BILL:"))
per=float(input("ENTER THE TOTAL NUMBER OF DINNING CUSTOMER:"))
member=input("IS ANY DINING CUSTOMER HAVE A MEMBERSHIP:").lower()
dis=0
if(member=="yes"):
    dis=bill*10/100 #memebership allows a special discount of 10%
elif(member=="no"):
    dis=0
fp=bill-dis
print("THE TOTAL BILL:",bill)
print("THE TOTAL DISCOUNT FOR MEMBERS:",dis)
print("THE FINAL PRICE PAYABLE:",fp)
print("THE PER HEAD COST TO BE PAID:",fp/per)
print("THANKS FOR VISITING OUR RESARAUNT")
