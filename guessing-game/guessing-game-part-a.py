from random import randint

rand_val = randint(0, 100)

while True:
  guess = int(input("Please enter your guess: "))
  if guess == rand_val:
    break
  elif guess < rand_val:
    print("Your guess was too low!")
  else:
    print("Your guess was too high!")

print("You guessed correctly with:", guess)