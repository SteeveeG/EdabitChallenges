# Link to Challenge: https://edabit.com/challenge/ZF9e922XuRaMu43Wp
def stair(count=0):
    if count == 0: print("___")
    spaces = count * 2
    stairs = ' ' * spaces
    stairs += "_\n"
    for x in range(count-1):
        spaces -= 2
        stairs += ' ' * spaces
        stairs += "_|\n"
    stairs += "_|"
    print(stairs)


stair(0)
stair(1)
stair(2)
stair(3)
stair(5)
stair(10)
stair(50)