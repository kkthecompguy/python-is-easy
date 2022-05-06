
def draw_field():
  for row in range(5):
    if row % 2 == 0:
      for col in range(5):
        if col % 2 == 0:
          if col != 4:
            print(" ", end="")
          else:
            print(" ")
        else:
          print("|", end="")
    else:
      print("-----")


player = 1
current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# current_field = [["c0 r0", "c0 r1", "c0 r2"], ["c1 r0", "c1 r2", "c1 r2"], ["c2 r0", "c2 r1", "c2 r2"]]

print(current_field)
while True:
  print("Players turn:", player)
  move_row = int(input("Please enter the row: "))
  move_column = int(input("Please enter the coulmn: "))

  if player == 1:
    # make move for player 1
    current_field[move_column][move_row] = "X"
    player = 2
  else:
    # make move for player 2
    current_field[move_column][move_row] = "O"
    player = 1
  print(current_field)
