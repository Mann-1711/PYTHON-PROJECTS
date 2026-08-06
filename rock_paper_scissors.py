#ROCK PAPER SCISSORS GAME IN PYTHON
player1=input("ENTER YOUR MOVE [ROCK,PAPER,SCISSORS]:").lower()
player2=input("ENTER YOUR MOVE[ROCK,PAPER,SCISSORS]:").lower()

if(player1==player2):
    print("THE GAME WAS A TIE")
    
if(player1=="rock" and player2=="paper"):
    print("PLAYER.2 WON AS ROCK GOT COVERED BY PAPER")
elif(player2=="scissors"):
    print("PLAYER.1WON AS ROCK SMASHED THE SCISSOR")

if(player1=="paper" and player2=="rock"):
    print("PLAYER.1 WON AS ROCK GOT COVERD BY PAPER")
elif(player2=="scissors"):
    print("PLAYER.2WON AS PAPER GOT CUT BY SCISSORS")

if(player1=="scissors" and player2=="paper"):
    print("PLAYER.1 WON AS PAPER GOT CUT BY SCISSORS")
elif(player2=="rock"):
    print("PLAYER.2 WON AS ROCK SMASHED SCISSORS")

    