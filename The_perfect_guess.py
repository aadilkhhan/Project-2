import random

guesses = 0
userGuess = None
random_number = random.randint(1 , 100)

while (userGuess != random_number):
    userGuess = int(input("Enter the number : "))
    guesses = guesses + 1

    if userGuess == random_number :
        print("You guessed correct number")

    else:
        if userGuess>random_number:
            print("You guesses wrong, Please choose smaller number")
        else:
            print("You guesses wrong, Please choose larger number")

print(f"No of guesses used is {guesses} guesses")

with open("hiscore.txt" , "r") as f:
    hiscore = int(f.read())

if guesses<hiscore:
    print("*****Congratulation you just broke the High score*******")
    with open("hiscore.txt" , "w") as f:
        f.write(str(guesses))


