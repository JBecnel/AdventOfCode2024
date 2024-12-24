import re

# used to determine if a gate starts with a z and a number
def starts_with_z_and_number(s):
    return bool(re.match(r'^z\d+', s))

def obtain_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    operations = []
    count = 0
    
    # get the gate values 
    for line in lines:
        if len(line) == 0:
            break
        # count to the line break
        count = count + 1
  
    # after the line break get the operations 
    z_count = 0   
    for line in lines[count+1:]:
        op_vals = line.split(" ")
        operations.append((op_vals[0], op_vals[1], op_vals[2], op_vals[4]))
        if starts_with_z_and_number(op_vals[4]):
            z_count += 1
    
    # a dictionary of known values, a list of operations, and the count of z values to find        
    return operations, z_count

# swap the output wires on the operations
def swap_output(wire1, wire2, operations):
    for i in range(len(operations)):
        ops = operations[i]
        output = ops[3]
        if output == wire1:
            operations[i] = (ops[0], ops[1], ops[2], wire2)
            
        if output == wire2:
            operations[i] = (ops[0], ops[1], ops[2], wire1) 

# return the operations that uses the wires and the gate
def find_in_operations(wire1, gate, wire2, operations):
    for ops in operations:
        if gate == ops[1]:
            if ops[0] == wire1 and ops[2] == wire2:
                return ops[3]
            if ops[0] == wire2 and ops[2] == wire1:
                return ops[3]
    return None

# see which need to be swapped
def check_adders(operations, num_bits):
    bit = 1
    misfits = []
    carry = find_in_operations("x00", "AND", "y00", operations)
    
    while bit < num_bits:
        xwire = "x" + ("0" if bit < 10 else "") + str(bit)
        ywire = "y" + ("0" if bit < 10 else "") + str(bit)
        zwire = "z" + ("0" if bit < 10 else "") + str(bit)
       
        
        ab_xor = find_in_operations(xwire, "XOR", ywire, operations)
        ab_and = find_in_operations(xwire, "AND", ywire, operations)
        
        carry_ab_xor_gate = find_in_operations(ab_xor, "XOR", carry, operations)
        if carry_ab_xor_gate is None:
            misfits.append(ab_xor)
            misfits.append(ab_and)
            swap_output(ab_xor, ab_and, operations)
            
            # reset
            bit = 1
            carry = find_in_operations("x00", "AND", "y00", operations)
            continue
        
        if carry_ab_xor_gate != zwire:
            misfits.append(carry_ab_xor_gate)
            misfits.append(zwire)
            swap_output(carry_ab_xor_gate, zwire, operations)
            
            # reset
            bit = 1
            carry = find_in_operations("x00", "AND", "y00", operations)
            continue
        
        carry_ab_and_gate = find_in_operations(ab_xor, "AND", carry, operations)
            
        carry = find_in_operations(ab_and,  'OR', carry_ab_and_gate, operations)
        bit = bit + 1
    return misfits    

def main():
    ops, z_count = obtain_input("puzzle24.dat")
    misfits = check_adders(ops, z_count-1)
    print("misfits " , ",".join(sorted(misfits)))
    
if __name__ == "__main__":
    main()