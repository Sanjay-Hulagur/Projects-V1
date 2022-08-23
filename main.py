print("Python is configured")
#Quiz Game
playing = input("Do you want to play a quiz? ")

if playing.lower() == "yes":
    print("now playing")
else:
    quit()

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct answer.")
    score += 1
else:
    print("your answer was wrong.")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("correct answer.")
    score += 1
else:
    print("your answer was wrong.")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct answer.")
    score += 1
else:
    print("your answer was wrong.")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("correct answer.")
    score += 1
else:
    print("your answer was wrong.")
answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("correct answer.")
    score += 1
else:
    print("your answer was wrong.")

print("You scored " + str(score) +" correct answers" )
print("You scored " + str((score / 5) * 100) +"%" )
#End of Quiz Game
