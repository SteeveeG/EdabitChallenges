# Link to Challenge : https://edabit.com/challenge/Zerwo2AENbvRZTe83
def tic_tac_toe(game):
    winner_sign = ""
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2]:
            winner_sign = game[i][0]
        elif game[0][i] == game[1][i] == game[2][i]:
            winner_sign = game[i][0]
    if game[0][0] == game[1][1] == game[2][2]:
        winner_sign = game[0][0]
    elif game[0][2] == game[1][1] == game[2][0]:
        winner_sign = game[0][2]
    elif winner_sign == "":
        print("It's a Tie")
        return
    print("Player ", 1 if winner_sign == "X" else 2, "wins")


tic_tac_toe(
    [["X", "O", "O"],
     ["O", "X", "O"],
     ["O", "#", "X"]])  # , "Player 1 wins")

tic_tac_toe(
    [["X", "O", "O"],
     ["O", "X", "O"],
     ["O", "#", "O"]])  # , "Player 2 wins")

tic_tac_toe(
    [["X", "O", "O"],
     ["O", "X", "O"],
     ["O", "O", "#"]])  # , "It's a Tie")

tic_tac_toe(
    [["X", "O", "O"],
     ["X", "X", "O"],
     ["X", "O", "#"]])  # , "Player 1 wins")

tic_tac_toe(
    [["X", "#", "O"],
     ["X", "X", "O"],
     ["#", "O", "#"]])  # , "It's a Tie")

tic_tac_toe(
    [["X", "X", "X"],
     ["X", "O", "O"],
     ["O", "O", "X"]])  # , "Player 1 wins")

tic_tac_toe(
    [["X", "O", "O"],
     ["X", "O", "O"],
     ["O", "X", "X"]])  # , "Player 2 wins")

tic_tac_toe(
    [["X", "O", "O"],
     ["X", "O", "O"],
     ["#", "X", "X"]])  # , "It's a Tie")

tic_tac_toe(
    [["X", "O", "O"],
     ["O", "O", "O"],
     ["#", "X", "X"]])  # , "Player 2 wins")
