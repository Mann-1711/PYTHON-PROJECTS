#This is a small  quiz game:
question=("what is the capital of India ?",
          "what is 10+7= ?",
          "Who is best football player of all time ?",
          "In which state of India do people speak Bengali ?",
          "Which country have  the highest population in the world ?")
answers=("delhi","17","cristiano ronaldo","west bengal","india")
i=0
marks=0
while i<5:
    print(question[i],)
    ianswer=input("enter your answers:").lower
    if(ianswer==answers[i]):
        print("correct")
        marks+=1
    else:
        print("wrong answers")
    i+=1
print("Your total score:",marks)
    