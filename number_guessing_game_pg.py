import random
secret = random.randint(1,100)
while True:
    guess = int(input("guess a number from (1,100): "))
    if guess==secret:
        print("Congratulations! You guessed the number.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")