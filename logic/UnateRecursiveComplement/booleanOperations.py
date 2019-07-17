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
    for cube in F:
        F_or_G.append(copyCube(cube))
    for cube in G:
        F_or_G.append(copyCube(cube))
    return F_or_G

def cofactor(F, x):
    index = abs(x) - 1
    F_cofactor_x = []
    if x > 0:
        for cube in F:
            if cube[index] == (0, 0):
                continue
            elif cube[index] == (0, 1):
                new_cube = copyCube(cube)
                new_cube[index] = (1, 1)
                F_cofactor_x.append(new_cube)
            elif cube[index] == (1, 0):
                continue
            elif cube[index] == (1, 1):
                new_cube = copyCube(cube)
                F_cofactor_x.append(new_cube)
            else:
                continue            
    elif x < 0:
        for cube in F:
            if cube[index] == (0, 0):
                continue
            elif cube[index] == (0, 1):
                continue
            elif cube[index] == (1, 0):
                new_cube = copyCube(cube)
                new_cube[index] = (1, 1)
            elif cube[index] == (1, 1):
                new_cube = copyCube(cube)
                F_cofactor_x.append(new_cube)
            else:
                continue            
    else:
        pass
    
    return F_cofactor_x

def positveCofactor(F, x):
    return cofactor(F, x)

def negativeCofactor(F, x):
    return cofactor(F, -x)

def oneVariableAND(x, P):
    """
        x is a non-zero integer denoting the variable of interest
        negative x ==> x_complement positive x ==> x
    """
    index = abs(x) - 1
    x_and_P = []
    if x > 0:
        for cube in P:
            if cube[index] == (0, 1):
                new_cube = copyCube(cube)
                x_and_P.append(new_cube)
            elif cube[index] == (1, 0):
                continue # don't add cube to AND list
            elif cube[index] == (1, 1):
                new_cube = copyCube(cube)
                new_cube[index] = (0, 1)
                x_and_P.append(new_cube)
            else:
                continue
        
    elif x < 0:
        for cube in P:
            if cube[index] == (1, 0):
                new_cube = copyCube(cube)
                x_and_P.append(new_cube)
            elif cube[index] == (0, 1):
                continue # don't add cube to AND list
            elif cube[index] == (1, 1):
                new_cube = copyCube(cube)
                new_cube[index] = (1, 0)
                x_and_P.append(new_cube)
            else:
                continue

    else:
        pass
        
    return x_and_P

def isZeros(F):
    pass

def allOnes(F):
    pass

def isOne(F):
    pass

def isOnlyOneCube(F):
    pass

def allCubeZeros(F):
    pass

def simpleNOT(F):
    pass

def selectSplitingVariableNot(F):
    pass

def NOT(F):
#     ##check if F is simple enough to complement it directly and quit
    if isZeros(F):
        return allOnes(F)
    elif isOne(F):
        return allCubeZeros(F)
    elif isOnlyOneCube(F):
        return simpleNOT(F)
    else:
        ## do recursion
        ## select variable for splitting
        x = selectSplitingVariableNot(F)
        P = NOT(positveCofactor(F, x))
        N = NOT(negativeCofactor(F, x))
        P = oneVariableAND(x, P)   # x and P
        N = oneVariableAND(-x, N)  # x_complement and N
        return OR(P, N)
    pass

def AND(F, G):
    return NOT(OR(NOT(F), NOT(G)))