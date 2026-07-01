# create 8 rows
for row in range(8):
  # create 8 columns
  for col in range(8):
    # create a square
    square = {"row": row, "col": col}
    # If it is the first row or the last row of the board
    if row == 0 or row == 7:
      # if it is an odd square
      if (col % 2) == 0:
        # set the square to white
        square["color"] = "white"
      else:
        square["color"] = "black"
    # if it is the second row or the sixth row of the board
    elif row == 1 or row == 6:
      # if it is an even square
      if (col % 2) == 0:
        # set the square to white
        square["color"] = "white"
      else:
        square["color"] = "black"
    # if it is the third or fifth row of the board
    elif row == 2 or row == 5:
      # if it is an odd square
      if (col % 2) == 0:
        # set the square to black
        square["color"] = "black"
      else:
        square["color"] = "white"
    # if it is the fourth row of the board
    elif row == 3 or row == 4:
      # if it is an even square
      if (col % 2) == 0:
        # set the square to black
        square["color"] = "black"
      else:
        square["color"] = "white"
    print(square)