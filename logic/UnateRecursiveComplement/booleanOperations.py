def copyCube(cube):
    copy = []
    for e in cube:
        copy.append(e)
    
    return copy

def zerosCube(cube):
    new_cube = []
    for e in cube:
        new_cube.append((0, 0))
    return new_cube

def onesCube(cube):
    new_cube = []
    for e in cube:
        new_cube.append((1, 1))
    return new_cube

def isZeroCube(cube):
    if (0, 0) in cube:
        return True
    else:
        return False

def isOneCube(cube):
    return onesCube(cube) == cube

def reduce(F):
    F_reduced = []
    ones = onesCube(F[0])
    if ones in F:
        F_reduced.append(ones)
        return F_reduced
    else:
        for cube in F:
            if (0, 0) not in cube:
                F_reduced.append(copyCube(cube))
            else:
                pass
    
    if len(F_reduced) == 0:
        F_reduced.append(zerosCube(F[0]))
    return F_reduced

def OR(F, G):
    F_or_G = []
    for cube in F:
        F_or_G.append(copyCube(cube))
    for cube in G:
        F_or_G.append(copyCube(cube))
    return F_or_G

def cofactor(F, x):
    index = abs(x) - 1
    F = reduce(F)
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
                F_cofactor_x.append(new_cube)
            elif cube[index] == (1, 1):
                new_cube = copyCube(cube)
                F_cofactor_x.append(new_cube)
            else:
                continue            
    else:
        pass

    if len(F_cofactor_x) == 0:
        F_cofactor_x.append(zerosCube(F[0]))
    else:
        F_cofactor_x = reduce(F_cofactor_x)
    
    return F_cofactor_x

def positiveCofactor(F, x):
    return cofactor(F, x)

def negativeCofactor(F, x):
    return cofactor(F, -x)

def oneVariableAND(x, P):
    """
        x is a non-zero integer denoting the variable of interest
        negative x ==> x_complement positive x ==> x
    """
    index = abs(x) - 1
    P = reduce(P)
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

    if len(x_and_P) == 0:
        x_and_P.append(zerosCube(P[0]))
    else:
        x_and_P = reduce(x_and_P)
        
    return x_and_P


def isZero(F):
    F_reduced = reduce(F)
    if len(F_reduced) != 1:
        return False
    else:
        return isZeroCube(F_reduced[0])

def allOnes(F):
    return [onesCube(F[0])]

def tautology(F):
    # TODO
    return False

def isOne(F):
    for cube in F:
        if isOneCube(cube):
            return True
    if tautology(F):
        return True
    return False

def isSingleCube(F):
    F_reduced = reduce(F)
    return len(F_reduced) == 1

def allZeros(F):
    return [zerosCube(F[0])]

def singleCubeNOT(cube):
    if isZeroCube(cube):
        return onesCube(cube)
    elif isOneCube(cube):
        return zerosCube(cube)
    else:
        cube_not = []
        for i in range(len(cube)):
            if cube[i] == (0, 0):
                return zerosCube(cube)
            elif cube[i] == (0, 1):
                new_cube = onesCube(cube)
                new_cube[i] = (1, 0)
                cube_not.append(new_cube)
            elif cube[i] == (1, 0):
                new_cube = onesCube(cube)
                new_cube[i] = (0, 1)
                cube_not.append(new_cube)
            elif cube[i] == (1, 1):
                pass
            else:
                pass
    
    cube_not = reduce(cube_not)
    return cube_not

def simpleNOT(F):
    F_reduced = reduce(F)
    return singleCubeNOT(F_reduced[0])

def selectSplitingVariableNot(F):
    positive_count = 0
    negative_count = 0
    num_of_variables = len(F[0])
    counts = []
    
    for i in range(num_of_variables):
        for cube in F:
            if cube[i] == (0, 1):
                positive_count += 1
            elif cube[i] == (0, 1):
                negative_count += 1
            else:
                pass
        counts.append((positive_count, negative_count))
        positive_count = 0
        negative_count = 0
    
    choosen_var = 0
    best_count = 0
    best_difference = num_of_variables
    for i in range(len(counts)):
        if counts[i][0] > 0 and counts[i][1] > 0:
            num_times_var_occured = counts[i][0] + counts[i][1]
            binate_difference = abs(counts[i][0] - counts[i][1])
            if num_times_var_occured > best_count:
                choosen_var = i
                best_count = num_times_var_occured
                best_difference = binate_difference
            elif num_times_var_occured == best_count:
                if binate_difference < best_difference:
                    choosen_var = i
                    best_count = num_times_var_occured
                    best_difference = binate_difference
                else:
                    pass
            else:
                pass
    
    if choosen_var == 0:
        for i in range(len(counts)):
            if counts[i][0] == 0:
                num_times_var_occured = counts[i][1]
            elif counts[i][1] == 0:
                num_times_var_occured = counts[i][1]
            else:
                continue
            
            if num_times_var_occured > best_count:
                choosen_var = i
                best_count = num_times_var_occured
            else:
                continue

    if choosen_var == 0:
        choosen_var = 1
    else:
        pass

    return choosen_var

def NOT(F):
#     ##check if F is simple enough to complement it directly and quit
    if isZero(F):
        return allOnes(F)
    elif isOne(F):
        return allZeros(F)
    elif isSingleCube(F):
        return simpleNOT(F)
    else:
        ## do recursion
        ## select variable for splitting
        x = selectSplitingVariableNot(F)
        P = NOT(positiveCofactor(F, x))
        N = NOT(negativeCofactor(F, x))
        P = oneVariableAND(x, P)   # x and P
        N = oneVariableAND(-x, N)  # x_complement and N
        return OR(P, N)
    pass

def AND(F, G):
    return NOT(OR(NOT(F), NOT(G)))