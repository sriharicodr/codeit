import random

roundNo = 1
myScore = 0

print("""HELLO!
WELCOME TO RANDOM NUMBER GAME.
YOU HAVE TO GET 5 OR MORE POINTS TO WIN.
IF YOU GET POINTS LESS THAN 5 YOU LOSE."""
          )
    
while roundNo<=10:
    print()
    print("ROUND: ",roundNo)
    print()
    ui = int(input("Please type any random number: "))
    print("Hint: The number can be any from 1-10!")
    print()

    cc = random.randint(1,10)

    if ui == cc:
        myScore+=1
        print("You got 1 point! 🎉")
        print()
        print("Your answer: ",ui)
        print("Real answer: ",cc)
    elif ui != cc:
        myScore -= 1
        print("You lost 1 point. 😥")
        print()
        print("Your answer: ",ui)
        print("Real answer: ",cc)
        roundNo += 1
print()
if myScore >= 5:
    print("Congratulations!! you won")
elif myScore < 5:
    print("You lost the game..Try again")
    









