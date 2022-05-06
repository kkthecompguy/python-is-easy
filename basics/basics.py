

for row in range(5):
  if row % 2 == 0:
    for col in range(1, 6):
      if col % 2 == 1:
        if col != 5:
          print(" ", end="")
        else:
          print(" ")
      else:
        print("|", end="")
  else:
    print("-----")


my_set = set()
my_set.add("US")
my_set.add("India")
my_set.add("Kenya")
my_set.add("US")
print(my_set)
print(dir(my_set))


vacation_spots = ["London", "Paris", "New York", "Utah", "Iceland"]

vacation_file = open("vacation", "w") # "r", "w", "a", "r+" -> read and append

for spot in vacation_spots:
  vacation_file.write(spot + "\n")

vacation_file.close()

vacation_file = open("vacation", "r")
first_line = vacation_file.readline()
print(first_line)
second_line = vacation_file.readline()
print(second_line)
# content = vacation_file.read()  # not efficient to call read on the whole file
# print(content)

for line in vacation_file: # this is the preferred way for memory efficiency
  print(line, end="")

vacation_file.close()

final_spot = "Thailand"

vacation_file = open("vacation", "a")
vacation_file.write(final_spot+"\n")
vacation_file.close()

vacation_file = open("vacation", "r")

for line in vacation_file:
  print(line, end="")


vacs = []
with open("vacation", "r") as vacation_file: # efficient way of opening writing and reading files as it is closed automatically
  for line in vacation_file:
    vacs.append(line)
    print(line)


print(vacs)
print(vacs.pop())