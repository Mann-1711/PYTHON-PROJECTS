# MOVIES LIST
movies=[]
a=input("input your fav movie 1:").lower()
movies.append(a)
a=input("input your 2nd movie:").lower()
movies.append(a)
a=input("enter your 3rd movie:").lower()
movies.append(a)
a=input("enter your 4th movie:").lower()
movies.append(a)
a=(input("enter your 5th movie")).lower()
movies.append(a)
d=input("do you wanna remove or add  any movie from your list[yes/no]:").lower()
if(d=="yes"):
    movies_remove=input("which movie do you wanna remove from list:").lower()#if the watcher wants to remove a movie
    movies_insert=input("which movie do you wanna add in your list:").lower()#if a watcher wants add a movie
    positions=int(input("where do you you wanna add your movie:"))#where the watcher wants to position his new movie
    movies.remove(movies_remove)
    movies.insert(positions,movies_insert)
    print(movies)
else:
    print(movies)

print("ENJOY YOUR MOVIES")