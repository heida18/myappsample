def game_rules(x,y):
    position = (x,y)
    if position == (1, 1):
        print("You can travel: (N)orth.")
        newpos = check_input("nN",position)
        print(newpos)
    elif position == (1, 2):
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        x, y = check_input("NnEeSs")
    elif position == (1, 3): 
        print("You can travel: (E)ast or (S)outh.")
        x, y = check_input("EeSs")
    elif position == (2, 1): 
        print("You can travel: (N)orth.")
        x, y = check_input("Nn")
    elif position == (2, 2):
        print("You can travel: (S)outh or (W)est.")
        x, y = check_input("SsWw")
    elif position == (2, 3): 
        print("You can travel: (E)ast or (W)est.")
        x, y = check_input("EeWw")
    elif position == (3, 2):
        print("You can travel: (N)orth or (S)outh.")
        x, y = check_input("NnSs")
    elif position == (3, 3):
        print("You can travel: (S)outh or (W)est.")
        x, y = check_input("SsWw")
    return newpos




