dBug = False

def read_puzzle_input(filename):
    registers = {}
    program = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('Register'):
                # Parse register line like "Register A: 729"
                parts = line.split(':')
                reg = parts[0][-1]  # Get the register letter
                value = int(parts[1].strip())
                registers[reg] = value
            elif line.startswith('Program'):
                # Parse program line like "Program: 0,1,5,4,3,0"
                nums = line.split(':')[1].strip()
                program = [int(x) for x in nums.split(',')]
    
    return registers, program

def process_instruction(opcode, operand, registers, instruction, output):
    combo_op = get_combo_operand(operand, registers)
    if opcode == 0:
        num = registers['A']     
        # adv: dividing by 2^operand shifts the bits to the right        
        # stores the result in A
        registers['A'] = num >> combo_op
    elif opcode == 1:
        # bxl bitwise XOR with operation with register B and literal operand
        registers['B'] = registers['B'] ^ operand
    elif opcode == 2:
        # bst combo operand modulo 8
        # and operation with 111
        registers['B'] = (combo_op & 7) 
    elif opcode == 3:
        # jnz instruction - move instruction index to operation if ['A'] is not 0
        if registers['A'] != 0:
            return operand
    elif opcode == 4:
        # bxc - compute bitwise xor of B and C registers
        registers['B'] = registers['B'] ^ registers['C']
    elif opcode == 5:
        # out - combo operand modulo 8, then output
        # if dBug:
        #     print(combo_op & 7)
        output.append(combo_op & 7)
    elif opcode == 6:
        num = registers['A']     
        # bdv: dividing by 2^operand shifts the bits to the right        
        # stores the result in B
        registers['B'] = num >> combo_op
    elif opcode == 7:
        # cdv : 
        num = registers['A']     
        # cdv: dividing by 2^operand shifts the bits to the right        
        # stores the result in B
        registers['C'] = num >> combo_op
        
    return instruction+ 2

# finds the correct combo operand based on the problem
def get_combo_operand(operand, registers):
     if operand <= 3:
         return operand
     else:
         if operand == 4:
             return registers['A']
         elif operand == 5:
             return registers['B']
         elif operand == 6:
             return registers['C']
    
     return -1 # invalid operand

# interprets the given list as a base 8 number with
# 8 spot, 64 spot, 512 spot, etc
def base_8(program):
    place = 8
    num = 0
    for p in program:
        num = num + place*p
        place = place * 8
    return num

def main():
    # Read the input file
    #file_name = 'puzzle17_sample1.dat'
    file_name = 'puzzle17.dat'
    registers, program = read_puzzle_input(file_name)

    

    # interpret the program as a number in base 8
    num = base_8(program)
    print(num)

    if dBug:
        debug_file = open('debug.txt', 'w')
        print(registers, file=debug_file)
        print(program, file=debug_file)
    
   
        # on viewing the debug file, we realize
        # that we are printing in the numbers in base 8, 
        # so we need the number in base 8
        # that matches the program input
        output = []
        reg_A = 0
        while output != program:
            output = []

            registers['A'] = reg_A
            registers['B'] = 0
            registers['C'] = 0

            instruction_index = 0
            while instruction_index < len(range(len(program))):
                opcode = program[instruction_index]
                operand = program[instruction_index + 1]
                # if dBug:
                #     print("pointer ", instruction_index)
                #     print("opcode ", opcode)
                #     print("operand : ", operand)
                
                instruction_index =  process_instruction(opcode, operand, registers, instruction_index, output)
                # if dBug:
                #     print( )            
                #     print(registers)
                #     print(output)
                #     print()

            if dBug:
                print("A", reg_A, file=debug_file)
                print("output", output, file=debug_file)

            
            reg_A = reg_A + 1
                    
    


        # Convert output list to comma-separated string
        result = ','.join(str(x) for x in output)
        print(result)
        print(reg_A)










if __name__ == "__main__":
    main()
