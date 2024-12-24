import re

dBug = True


def obtain_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    values = {}
    operations = []
    count = 0
    
    # get the gate values 
    for line in lines:
        if len(line) == 0:
            break
        # count to the line break
        count = count + 1
        gate_value = line.split(":")
        values[gate_value[0]] = (gate_value[1].strip() == '1')
    
    # after the line break get the operations 
    z_count = 0   
    for line in lines[count+1:]:
        op_vals = line.split(" ")
        operations.append((op_vals[0], op_vals[1], op_vals[2], op_vals[4]))
        if starts_with_z_and_number(op_vals[4]):
            z_count += 1
    
    # a dictionary of known values, a list of operations, and the count of z values to find        
    return values, operations, z_count

# used to determine if a gate starts with a z and a number
def starts_with_z_and_number(s):
    return bool(re.match(r'^z\d+', s))

# this method performs the operations on the values 
def perform_operations(values, operations, known_z):
    for oper in operations:
        op = oper[1]
        wire1 = oper[0]
        wire2 = oper[2]
        output = oper[3]
        
        if output in values:
            continue
        
    
        if op == "AND":
            if wire1 in values and wire2 in values:
                values[output] = values[wire1] and values[wire2]
            elif wire1 in values and values[wire1] == 0:
                values[output] = False
            elif wire2 in values and values[wire2] == 0:
                values[output] = False
            if starts_with_z_and_number(output):
                if output in values:
                    known_z[output] = values[output]
        
            
        elif op == "OR":
            if wire1 in values and wire2 in values:
                values[output] = values[wire1] or values[wire2]
            elif wire1 in values and values[wire1] == 1:
                values[output] = True
            elif wire2 in values and values[wire2] == 1:
                values[output] = True
            if starts_with_z_and_number(output):
                if output in values:
                    known_z[output] = values[output]
        
        else:  # XOR:
            if wire1 in values and wire2 in values:
                values[output] = (values[wire1] != values[wire2])
                if starts_with_z_and_number(output):
                    known_z[output] = values[output]
           

def main():
    file_name = "puzzle24_sample.dat"
    file_name = "puzzle24.dat"
    values, operations, num_z = obtain_input(file_name)

    
    # find all the z gates
    known_z = { }
    while len(known_z) != num_z:
        perform_operations(values, operations, known_z)

    # sort by the z value    
    sorted_known_z = dict(sorted(known_z.items(), key=lambda item: int(item[0][1:])))
    if dBug:
        print(sorted_known_z)
    
    result = 0
    num = 1
    for key, val in sorted_known_z.items():
        if val:
            result = result  + num
        num = 2 * num     
    print(result)
if __name__ == '__main__':
    main()
    