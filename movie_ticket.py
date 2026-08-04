# MOVIE THEATER
print("WELCOME TO OUR MOVIE THEATER")
gen=input("ENTER THE MOVIE GENRE YOU WANNA WATCH[HORROR,ACTION,COMEDY]:").lower()
age=float(input("ENTER YOUR CURRENT AGE:"))
time=input("ENTER THE SHOWTIME YOU WOULD PREFFERP[MORNING,EVENING,NIGHT]:")#price: morning=200,evning=400,night=300
num=float(input("ENTER THE NUMBER OF TICKETS YOU WANT TO BOOK:"))# higher the number of tickets the higher the discount
price=0
if(gen=="horror"and age<15 or age==15): # their is an age restriction of 15 years on horror movies
    print("SORRY YOU ARE NOT ELIGIBLE FOR THIS MOVIE AND")
elif(gen=="action" or gen=="comedy" or gen=="horror" and age>15):
    print("YOU ARE GONNA  WATCH MOVIE FULL OF:",gen)
    if(time=="morning"):
        price=200
    elif(time=="evening"):
        price=400
    elif(time=="night"):
        price=300
tp=price*num # total price of tickets
if(num>1 or num==1 and num<3):
    dis=0
elif(num>4 or num==4 and num<7):
    dis=tp*10/100
elif(num>7 or num==7):
    dis=tp*20/100

if(price>0):
    print("THE TOTAL NUMBER OF TICKETS BOOKED:",num)
    print("THE TOTAL PRICE OF TICKETS:",tp)
    print("THE DISCOUNT ON TICKETS:",dis)
    print("THE FINAL PRICE TO BE PAID:",tp-dis)
print("THANKS FOR COMING TO OUR THEATER")







