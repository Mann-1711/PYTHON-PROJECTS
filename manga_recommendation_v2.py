# So this is the version 2 of my manga recommendation system which i made few months ago it was purely made using if/else statements.
# Now I'm gonna make this recommender again with the new things i had leant.
#print("WELCOME TO MY MANGA RECOMMENDER PROGRAM ")
#print("\nPLEASE SELECT YOUR PREFFERNCE FOR FINDING BEST MANGA'S TO READ")
#genre=input("ENTER THE GENRE WHICH INTEREST YOU THE MOST[ACTION,SUPERNATURAL,ROMANCE,SPORTS]:").lower()
#length=input("ENTER THE LENGTH YOU WOULD PREFFER FOR MANGA[SHORT(100-400),MEDIUM(500-800),LONG(800-1,000)]:").lower()
#story=input("THE OVERALL MOOD OF STORY YOU WOULD LIKE TO READ[SAD,HAPPY,MINDBENDING]:").lower()
manga_database = [
    {"title": "One Piece", "genre": "action", "length": "long", "rating": 9.5},
    {"title": "Naruto", "genre": "action", "length": "long", "rating": 9.0},
    {"title": "Attack on Titan", "genre": "action", "length": "long", "rating": 9.4},
    {"title": "Demon Slayer", "genre": "action", "length": "medium", "rating": 8.7},

    {"title": "Jujutsu Kaisen", "genre": "supernatural", "length": "medium", "rating": 8.8},
    {"title": "Death Note", "genre": "supernatural", "length": "short", "rating": 9.3},
    {"title": "Tokyo Ghoul", "genre": "supernatural", "length": "medium", "rating": 8.6},
    {"title": "Blue Exorcist", "genre": "supernatural", "length": "long", "rating": 8.2},

    {"title": "Kaguya-sama: Love Is War", "genre": "romance", "length": "long", "rating": 9.1},
    {"title": "Horimiya", "genre": "romance", "length": "short", "rating": 8.8},
    {"title": "Fruits Basket", "genre": "romance", "length": "medium", "rating": 8.7},
    {"title": "Blue Box", "genre": "romance", "length": "medium", "rating": 8.5},

    {"title": "Blue Lock", "genre": "sports", "length": "long", "rating": 9.0},
    {"title": "Haikyuu!!", "genre": "sports", "length": "long", "rating": 9.3},
    {"title": "Slam Dunk", "genre": "sports", "length": "medium", "rating": 9.2}
]
def show_manga(list,idx):
    while(idx<len(list)):
        print(list[idx])
        idx+=1
show_manga(manga_database,0)