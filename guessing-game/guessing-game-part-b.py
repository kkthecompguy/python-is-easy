from random import random
import time

rand_val = random() # 0.0 <= n < 1.0

upper = 1.0
lower = 0.0
counter = 0

current_time = time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID)
while True:
  guess = (upper + lower) / 2
  if guess == rand_val:
    break
  elif guess < rand_val:
    lower = guess
  else:
    upper = guess
  counter += 1
end_time = time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID)
print("It took us:", end_time - current_time)

print(guess)
print(counter)

