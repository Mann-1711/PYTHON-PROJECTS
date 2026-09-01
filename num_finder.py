#THIS IS A SMALL NUMBER FINDER.
a=[1,2,3,4,5,6,7,8,9,10,]
i=0
x=int(input("ENTER THE NUMBER YOU WANT TO FIND FROM LIST:"))
while i<=len(a):
    if(x==a[i]):
     print("find at idx:",i)
     break
    else:
       print("finding...")
    i+=1
