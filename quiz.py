print("Welcome to my computer quiz!")
answer = input("will you like to play? ")
if answer.lower() != "yes":
    quit()
else:
    print("Okay! Let's Play!")

score = 0

answer = input("what does CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("what does RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")    

answer = input("what does ROM stand for? ").lower()
if answer == "read only memory":
    print("correct!")
    score += 1
else:
    print("incorrect!") 

answer = input("what does GUI stand for? ").lower()
if answer == "graphic user interface":
    print("correct!")
    score += 1
else:
    print("incorrect!") 

answer = input("what does UI stand for? ").lower()
if answer == "user interface":
    print("correct!")
    score += 1
else:
    print("incorrect!") 

print(f"Your score is {score/5} %")
 
