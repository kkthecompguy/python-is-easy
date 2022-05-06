participant_number = 2
participant_data = []
output_file = "participant_data.txt"

registered_participant = 0

# while registered_participant < participant_number:
#   temp_part_data = [] # name, country of origin, age
#   name = input("Please enter your name: ")
#   country = input("Please enter country of origin: ")
#   age = int(input("Please enter your age: "))

#   temp_part_data.append(name)
#   temp_part_data.append(country)
#   temp_part_data.append(age)
#   participant_data.append(temp_part_data)

#   registered_participant += 1


for participant in participant_data:
  with open(output_file, "a") as file:
    for data in participant:
      file.write(str(data))
      file.write(" ")
    file.write("\n")


input_file = "participant_data.txt"
input_list = []

with open(input_file, "r") as file:
  for line in file:
    temp_input = line.strip("\n").split()
    input_list.append(temp_input)

age_dict = {}

for part in input_list:
  temp_age = int(part[-1])
  if temp_age in age_dict:
    age_dict[temp_age] += 1
  else:
    age_dict[temp_age] = 1

print(age_dict)

# input_list = []
# input_file = open("participant_data.txt", "r")
# for line in input_file:
#   temp_input = line.strip("\n").split()
#   print(temp_input)
#   input_list.append(temp_input)

# input_file.close()

print(input_list)