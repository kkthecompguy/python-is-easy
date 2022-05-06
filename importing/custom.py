import random
import time
import math

# random.seed(1)
randint = random.randint(0, 10) # start <= N <=end
print(randint)

randfloat = random.random() # 0.0 <=N < 1.0
print(randfloat)

randuniform = random.uniform(1, 111) # start <= N <= end
print(randuniform)

numbers_list = [x for x in range(1, 50)]
# print(numbers_list)

picked = random.choice(numbers_list)
print(picked)

random.shuffle(numbers_list)

# print(numbers_list)

current_time = time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID)
print(time.CLOCK_PROCESS_CPUTIME_ID)
print("Hello world")
print("world")
end_time = time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID)
print(end_time - current_time)

# for i in range(10):
#   print(i)
#   time.sleep(1)

val = 3.14
sqrt_val = math.sqrt(val) # val^2
print(sqrt_val)

exp_val = math.exp(val) # e^val
print(exp_val)

fact_val = math.factorial(math.floor(val)) # 5! = 5*4*3*2*1
print(fact_val)

sin_val = math.sin(val)
print(sin_val)

floor_val = math.floor(val)
print(floor_val)

ceil_val = math.ceil(val)
print(ceil_val)