#MANGA RECOMMENDER
#THIS IS A PROGRAM TO RECOMMEND DIFFERENT MANGA'S BASED ON YOUR PERSONAL PREFFRENCE.
print("WELCOME TO MY PROGRM")
print("\nPLEASE SELECT YOUR PREFFERNCE FOR FINDING BEST MANGA'S TO READ")
genre=input("ENTER THE GENRE WHICH INTERESR YOU THE MOST[SHONEN,SENIN,SPORTS]:").lower()
length=input("ENTER THE LENGTH YOU WOULD PREFFER FOR MANGA[SHORT(100-400),MEDIUM(500-800),LONG(800-1,000)]:").lower()
story=input("THE OVERALL MOOD OF STORY YOU WOULD LIKE TO READ[SAD,HAPPY,MINDBENDING]:").lower()
#NOW FROM HERE ON ARE ALL THE CASES FOR DIFFERNT MANGA'S.

#START OF SHONEN MANGA'S CASES:
if(genre=="shonen"):
    if(length=="short"):
        if(story=="happy"):
            print("'SPY X FAMILY' IS A GOOD CHOICE.")

        elif(story=="sad"):
            print("'YOUR LIE IN APRIL' IS A  HECK OF A MANGA.")
        elif(story=="mindbending"):
            print("'ERASED' IS THE MANGA YOU WOULD LOVE.")

    if(length=="medium"):
      if(story=="happy"):
          print("'BLEACH' IS THE BEST MANGA FOR YOUR PREFFERENCE.")

      elif(story=="sad"):
          print("'ASSAINATION CLASSROOM' WOULD BE AWESOME CHOICE FOR YOU.")
      elif(story=="mindbending"):
          print("'THE PROMISE NEVERLAND' WOULD BE THHE BEST PICK FOR YOU.")

    if(length=="long"):
        if(story=="happy"):
            print("'ONE PEICE' IS A CLASSIC YOU MUST CHECK OUT.")

        elif(story=="sad"):
            print("'NARUTO' IS A STORY FULL OFF EMOTION.")
        elif(story=="mindbending"):
            print("'ATTACK ON TITAN' IS A PERFECT PICK.")
#END OF THE SHONEN CASES.
#START OF SENIN CASES:
if(genre=="senin"):
    if(length=="short"):
        if(story=="happy"):
            print("'LOOK BACK' IS A CRAZY GGOOD OPTION.")

        elif(story=="happy"):
            print("'ERI' IS THE MANGA YOU ARE LOOKING FOR.")
        elif(story=="mindbending"):
            print("'THE FLOWER OF EVIL' IS A SUPERB MANGA.")

    if(length=="medium"):
        if(story=="happy"):
            print("'PLUTO' IS A SUPERB CHOICE.")

        elif(story=="sad"):
            print("'A SILENT VOICE' IS THE ONE TO READ.")
        elif(story=="mindbending"):
            print("'20TH CENTRY BOYS' IS AN ABSOLUTE MIND BOGGELING STORY.")

    if(length=="long"):
        if(story=="happy"):
            print("'KINGDOM' IS MANGA TOO READ")

        elif(story=="sad"):
            print("'BERSERK' IS THE A MASTERPEICE TO READ.")
        elif(story=="mindbending"):
            print("'MONSTER' IS THE MANGA TO CHECKOUT.")
#END OF SENIN MANGA'S CASES.
if(genre=="sports"):
    if(length=="short"):
        if(story=="happy"):
            print("'PINK PONG' IS A LOVELY SPORTS STORY.")

        elif(story=="sad"):
            print("'BLUE BOX' IS A GO FOR IT.")
        elif(story=="mindbending"):
            print("'THE CLIMBER' IS THE PEAK.")

    if(length=="medium"):
        if(story=="happy"):
         print("'HAIKYUU' IS A AWESOME MANGA.")

        elif(story=="sad"):
            print("'REAL' IS THE MANGA YOU WOULD LOBE TO READ.")
        elif(story=="mindbending"):
            print("'BLUE LOCK' IS A MANGA FOR EGOIST.")

    if(length=="long"):
        if(story=="happy"):
            print("'SLAM DUNK' IS THE MANGA YOU ARE LOOKING FOR.")

        elif(story=="sad"):
            print("'ASHITA NA JOE' IS A MANGA TO CONSIDER.")
        elif(story=="mindbending"):
            print("'HAJIME NO IPPO' IS A MANGA THQT CHANGE PEOPLE'S LIFE.")
#END  OF SPORTS CASES.
else:
    print("SORRY WE DONT HAVE ANY MANGA FOR YOUR PREFFERENCE.")
print("\nTHANKS FOR BEING HERE AND USE MY PROGRAM")
        

