import random
number = int(random.random()*10)
guess_limit = 3
print("Guess the number between '0-9', you have three chances!")
print()
i = 1
while i<=guess_limit:
    guess = int(input(f"Guess {i}: "))
    if guess == number:
        print(f"You guessed right!")
        break
    i+=1

if i>3:
    print("Game Over!")
    print(f"The number was {number}")