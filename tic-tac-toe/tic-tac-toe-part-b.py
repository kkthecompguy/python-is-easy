
def draw_field(field: list):
  for row in range(5): # 0, 1, 2, 3, 4
                      # 0, ., 1, ., 2
    if row % 2 == 0: # 0, 2, 4
      prac_row = row // 2 # 0, 1, 2
      for col in range(5): # 0, 1, 2, 3, 4
                           # 0, ., 1, ., 2
        if col % 2 == 0: # 0, 2, 4
          prac_col = col // 2 # 0, 1, 2
          if col != 4:
            print(field[prac_col][prac_row], end="")
          else:
            print(field[prac_col][prac_row])
        else:
          print("|", end="")
    else:
      print("-----")


player = 1
current_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# current_field = [["c0 r0", "c0 r1", "c0 r2"], ["c1 r0", "c1 r2", "c1 r2"], ["c2 r0", "c2 r1", "c2 r2"]]

draw_field(current_field)
while True:
  print("Players turn:", player)
  move_row = int(input("Please enter the row: "))
  move_column = int(input("Please enter the coulmn: "))

  if player == 1:
    # make move for player 1
    if current_field[move_column][move_row] == " ":
      current_field[move_column][move_row] = "X"
      if (current_field[0][0] == "X" and current_field[0][1] == "X" and current_field[0][2] == "X") or (current_field[1][0] == "X" and current_field[1][1] == "X" and current_field[1][2] == "X") or (current_field[2][0] == "X" and current_field[2][1] == "X" and current_field[2][2] == "X") or (current_field[0][0] == "X" and current_field[1][1] == "X" and current_field[2][2] == "X") or (current_field[2][0] == "X" and current_field[1][1] == "X" and current_field[0][2] == "X") or (current_field[0][0] == "X" and current_field[1][0] == "X" and current_field[2][0] == "X") or ((current_field[0][1] == "X" and current_field[1][1] == "X" and current_field[2][1] == "X")) or (current_field[0][2] == "X" and current_field[1][2] == "X" and current_field[2][2] == "X"):
        print("Player 1 won")
        draw_field(current_field)
        break
      player = 2
  else:
    # make move for player 2
    if current_field[move_column][move_row] == " ":
      current_field[move_column][move_row] = "O"
      if (current_field[0][0] == "O" and current_field[0][1] == "O" and current_field[0][2] == "O") or (current_field[1][0] == "O" and current_field[1][1] == "O" and current_field[1][2] == "O") or (current_field[2][0] == "O" and current_field[2][1] == "O" and current_field[2][2] == "O") or (current_field[0][0] == "O" and current_field[1][1] == "O" and current_field[2][2] == "O") or (current_field[2][0] == "O" and current_field[1][1] == "O" and current_field[0][2] == "O") or (current_field[0][0] == "O" and current_field[1][0] == "O" and current_field[2][0] == "O") or ((current_field[0][1] == "O" and current_field[1][1] == "O" and current_field[2][1] == "O")) or (current_field[0][2] == "O" and current_field[1][2] == "O" and current_field[2][2] == "O"):
        print("Player 2 won")
        draw_field(current_field)
        break
      player = 1
  draw_field(current_field)
