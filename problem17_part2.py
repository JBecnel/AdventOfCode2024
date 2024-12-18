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

# Here is the breakdown of what's happening.
# Notice that we only process one octal digit at a time.
# A = [x1,x2,...., xn] in oct
# 2,4
# B = xn  (B is 0,1,2,3,4,5,6,7)
# 1,3
# B = xn XOR 011   (B is 4, 2, 1, 0, 7, 6, 5, 4)
# 7, 5
# C  = A >> B 
# 0, 3 
# A = [x1,x2,....,xn-1] (lose digit) 
# 4,1
# B = B XOR C  ???
# 1,5
# B = B XOR 101 
# 5, 5
# write B
# 3, 0
# go to start

def invert(program, reg):
        # perform a BSF to find hte solutions
        queue = [(15, 0)] # number of instructions to consider, starting value for a
                          # start with only the last instruction and work backwards
        answers = [] # potential values for the A that lead to the desired output (there should be 8)
        while queue:  # while the queue is not eimpty
            i, A_val = queue.pop(0)
            if i >= 0:
                for oct in range(8):  # possible next octal digit
                    # shift the current value of a over 3 to make room for next oct
                    next_A = (A_val << 3) + oct
                   
                    # get the output from the program given the 
                    # program instructions (program)
                    # starting value for a
                    output = run_program(reg, program, next_A)
                    if output == program[i:]: # if the output matches the program instructions (starting at i)
                        if i == 0:
                            answers.append(next_A)
                        queue.append((i-1, next_A))

        print("answer", min(answers)) # take the min of the 8 answers

# process the given instruction
# opcode - operations to conduct
# operand - designates values to apply it to
# registers - values of the registry
# instruction - index of current instruction
# output - current output
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
        # stores the result in c
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


def run_program(registers, program, value):
    output = []

    registers['A'] = value
    registers['B'] = 0
    registers['C'] = 0

    instruction_index = 0
    while instruction_index < len(range(len(program))):
        # grabe the op code and operand
        opcode = program[instruction_index]
        operand = program[instruction_index + 1]
        # process the instruction and return the new index
        instruction_index =  process_instruction(opcode, operand, registers, instruction_index, output)
    # output of program
    return output
    
def main():
    # Read the input file
    file_name = 'puzzle17_sample1.dat'
    file_name = 'puzzle17.dat'
    registers, program = read_puzzle_input(file_name)

    invert(program, registers)

    if dBug:
        debug_file = open('debug.txt', 'w')
        print(registers, file=debug_file)
        print(program, file=debug_file)
        print(len(program), file=debug_file)
    
   
    # find the one that gives us the output
    output = []
    # displays some values for pattern recognition    
    if dBug:
        for reg_A in range(pow(8,len(program)), pow(8, len(program)+1) ):
        #for reg_A in range(num, num+1):
            value = reg_A    
            #if dBug:
            #value = pow(8, reg_A)

            output = run_program(registers,program, value)
            if dBug and len(output) > 0:
                print("A", reg_A, file=debug_file)
                print("output", output, file=debug_file)

            
            if output == program:
                print(reg_A)
                    



    










if __name__ == "__main__":
    main()
