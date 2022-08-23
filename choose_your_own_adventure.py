print("Python is configured4")
name = input("Type your name: ")
print("Welcome", name)

answer = input("You are on a dirt road, after walking for 2 hours, you are running out of water. what do you want to do (keep walking/turn back/try to search water)").lower()
if answer == "keep walking":
    print("you went too far to return and you ran out of water - You loose.")
elif answer == "turn back":
    print("you should have chosen better, on the way back you are met with goblins and they take all your gold. - You loose")
elif answer == "try to search water":
    answer2 = input("You took a left turn and clibed a hill - you see a pond with muddy water what do you do? (look for a way to clean water/ make the water flow to an empty hole)").lower()
    if answer2 == "look for a way to clean water":
        aaaa = input("you clean the water with you shirt, do you drink the water.(yes/no)").lower()
        if aaaa == "yes":
            print("You thirst is quenched - You win")
        elif aaaa == "no":
            print("wrong choice - you are thirsty - remember !! you loose!")
    elif answer2 == "make the water flow to an empty hole":
        answer3 = input("you make the water flow and after it rests you get clean water? Do you drink the water? (yes/no)").lower()
        if answer3 == "yes":
            print("You thirst is quenched - You win")
        elif answer3 == "no":
            print("you loose!")
else:
    print("Invalid option - Please choose again")
