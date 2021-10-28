import random

guesses_taken = 0
number = random.randint(1, 10)

print("Hi!, What is your name?")
name = input()

print("Well,", name, ", i'm guessing the number, from 1 to 10")

for guesses_taken in range(3):
    print("Try guess! Enter number:")

    while True:
        try:
            guess = int(input())
        except ValueError:
            print("latter's entered")
            continue
        else:
            break

    if guess < number:
        print("Your number is too small.")

    if guess > number:
        print("Your number is too large.")

    if guess == number:
        print("Well done! ", name, " you did it in", guesses_taken + 1, " attempts")
        break

if guess != number:
    number = str(number)
    print("Alas. I made a number: ", number)
