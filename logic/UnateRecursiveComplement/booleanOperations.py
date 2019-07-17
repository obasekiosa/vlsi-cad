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
    """ x is a non-zero integer denoting the variable of interest negative x ==> x_complement positive x ==> x """
    index = abs(x) - 1
    x_and_p = []
    if x > 0:
        for cube in P:
            new_cube = copyCube(cube)
            if cube[index] == (0, 1):
                x_and_p.append(new_cube)
            elif cube[index] == (1, 0):
                continue # don't add cube to AND list
            elif cube[index] == (1, 1):
                new_cube[index] = (0, 1)
                x_and_p.append(new_cube)
            else:
                continue
        
    elif x < 0:
        for cube in P:
            new_cube = copyCube(cube)
            if cube[index] == (1, 0):
                x_and_p.append(new_cube)
            elif cube[index] == (0, 1):
                continue # don't add cube to AND list
            elif cube[index] == (1, 1):
                new_cube[index] = (1, 0)
                x_and_p.append(new_cube)
            else:
                continue

    else:
        pass
        
    return x_and_p

def NOT(F):
    pass

def AND(F, G):
    return NOT(OR(NOT(F), NOT(G)))