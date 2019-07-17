import booleanOperations

def generateCube(variable_list, num_of_variables):
    cube = []
    for i in range(num_of_variables):
        index = i + 1
        if index in variable_list:
            cube.append((0, 1))
        elif -index in variable_list:
            cube.append((1, 0))
        else:
            cube.append((1, 1))

    return cube

def writeOuput(output_function):
    num_of_variables = 0 
    num_of_cubes = len(output_function)
    for e in output_function[0]:
        num_of_variables += 1
    
    destination_file = open(destination_file_name, "w+")
    output = str(num_of_variables) + "\n"
    destination_file.write(output)
    output = str(num_of_cubes) + "\n"
    destination_file.write(output)

    output = ''
    num_of_cube_variables = 0
    for cube in output_function:
        for i in range(num_of_variables):
            index = i + 1
            if cube[i] == (0, 1):
                output += "  " + str(index)
                num_of_cube_variables += 1
            elif cube[i] == (1, 0):
                output += " " + str(-index)
                num_of_cube_variables += 1
            else:
                continue
        if output != '':
            output = str(num_of_cube_variables) + " " + output + "\n"
        else:
            output = str(num_of_cube_variables) + "\n"

        destination_file.write(output)
    
    destination_file.close()
    
    return


f = open(file_name, "r")
line = f.readline()
num_of_variables = int(line)
line = f.readline()
num_of_cubes = int(line)
 
boolean_function = []

for i in range(num_of_cubes):
    line = f.readline()
    line = line.split(' ')
    num_of_cube_variables = int(line[0])
    cube = []
    for e in line[1:]:
        if e != '':
            cube.append(int(e))
    boolean_function.append(generateCube([cube], num_of_variables))

f.close()

output_function = booleanOperations.NOT(boolean_function)
writeOuput(output_function)

