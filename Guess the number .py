#while loop
count = 0
while count<9:
    print("Number:", count)
    count = count+1
print("Good")
#new while loop
import random
n = 50
to_be_guessed = int(n * random.random())
guess = 0
while guess != to_be_guessed:
    guess = int(input("New Number:"))
    if guess > 0:
        if guess > to_be_guessed:
            print("New Number too large")
        elif guess < to_be_guessed:
            print("New Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")