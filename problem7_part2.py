# concatenate two numbers
def numConcat(num1, num2):
     # find number of digits in num2
     digits = len(str(num2))
     # add zeroes to the end of num1
     num1 = num1 * (10**digits)
     # add num2 to num1
     num1 += num2
     return num1
 

# the following returns the teranary 
# sequence representing an integer with the 
# given number of digits
def create_operation_sequence(number, num_digits):
    seq = [0] * num_digits
    index = 1
    while number > 0:
        seq[-index] = number % 3
        number = number // 3
        index += 1
    
    return seq

# performs the operations on the given number and returns the result
# returns True if we hit the target
# we should have 1 move number than operation
def perform_operation(nums, ops, target):
    total = nums[0]
    for op_index in range(len(op_seq)):
        num2 = nums[op_index+1]  # next number
        if ops[op_index] == 0:
            total *= num2
        elif op_seq[op_index] == 1:
            total += num2
        else: # concatenation of numbers
            total = numConcat(total, num2)
            
        if (total > target):
            return False
    
    return (total == target)
            

# read the file puzzle7_samples a dat one line at a time
file_name = 'puzzle7_sample.dat'
file_name = 'puzzle7.dat'
result = []
num_list = []
with open(file_name, 'r') as puzzle_file:
    for line in puzzle_file:
        colon_split = line.split(':')
        result.append(int(colon_split[0].strip()))
        
        nums = colon_split[1].strip().split(' ')
        num_list.append([int(num) for num in nums])


result_set = set()
for k in range(len(result)):
    # the total number of operations is one fewer than the numbers
    num_operations = len(num_list[k])-1
    # we use ternary   from 0 to 3^(num_ops)-1
    # to traverse all possible operation combination
    # the three legal operations are multiplication, concatenation, and addition
    total_combination = pow(3,num_operations) 
    operation = 0
    result_found = False
    while (operation < total_combination) and (not result_found):
        op_seq = create_operation_sequence(operation, num_operations)
        #print(operation, op_seq)

        # perform the operations indication by the ternary representation
        # of tne number operation with
        # 0 - multiplication
        # 1 - addition
        # 2 - concatenation
        # perform the operations on the sequence of numbers (staying under the result)
        result_found = perform_operation(num_list[k], op_seq, result[k])

            
        if (result_found):
            result_set.add(result[k])
            #print(num_list[k], result[k], op_seq)

        operation = operation + 1 

# total up the result set
sum = 0
for x in result_set:
    sum = sum + x

print(sum)

    
        
    