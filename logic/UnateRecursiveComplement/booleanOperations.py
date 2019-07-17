def copyCube(cube):
    copy = []
    for e in cube:
        if e == (0, 1):
            copy.append((0, 1))
        elif e == (1, 0):
            copy.append((1, 0))
        elif e == (1, 1):
            copy.append((1, 1))
        elif e == (0, 0):
            copy.append((0, 0))
        else:
            print("Invalid entry")
    
    return copy

def OR(F, G):
    F_or_G = []
    F_or_G.append(F)
    F_or_G.append(G)
    return F_or_G

def oneVariableAND(x, P):
    pass

def NOT(F):
    pass

def AND(F, G):
    return NOT(OR(NOT(F), NOT(G)))