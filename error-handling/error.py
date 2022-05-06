

try:
  print(int("hello"))
except ValueError as e:
  print("got a ValueError")
except:
  print("Other type of exception")
finally:
  print("finally")