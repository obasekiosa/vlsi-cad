import sys
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
            output = str(num_of_cube_variables) + output + "\n"
        else:
            output = str(num_of_cube_variables) + "\n"

        destination_file.write(output)
        output = ''
        num_of_cube_variables = 0
    
    destination_file.close()
    return

if len(sys.argv) != 2:
    print(" 1 argument needed")
    exit()
elif sys.argv[1].count('.') != 1:
    print("file extention needed")
    exit()
elif sys.argv[1].split(".")[1].lower() != "pcn":
    print(".pcn file needed")
    exit()
else:
    pass


    
file_name = sys.argv[1]
destination_file_name = "out_" + file_name

f = open(file_name, "r")
line = f.readline()
num_of_variables = int(line)
line = f.readline()
num_of_cubes = int(line)
 
boolean_function = []

for i in range(num_of_cubes):
    line = f.readline()
    line = line[:-1]
    line = line.split(' ')
    num_of_cube_variables = int(line[0])
    cube = []
    for e in line[1:]:
        if e != '':
            cube.append(int(e))
    pcn_cube = generateCube(cube, num_of_variables)
    boolean_function.append(pcn_cube)

f.close()

output_function = booleanOperations.NOT(boolean_function)
writeOuput(output_function)

