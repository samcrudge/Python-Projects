import random

hidden = random.randrange(1, 100)
guess = int(input("Please enter your guess: "))

while guess == hidden:
    print("hit!")
    print("I was kidding")
if guess < hidden:
    print("your guess is too low")
    exit()
else:
    print("your guess is too high")
    exit()
