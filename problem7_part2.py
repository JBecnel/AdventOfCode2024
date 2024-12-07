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
    num_operations = len(num_list[k])-1
    # for each ternary number  from 0 to 3^(n-1)-1
    # calculate the result of the numbers 
    # the three legal operations are multiplication, concatenation, and addition
    total_combination = pow(3,num_operations) 
    operation = 0
    while operation < total_combination:
        # perform the operations indication by the ternary representation
        # of tne number operation with
        # 0 - multiplication
        # 1 - addition
        # 2 - concatenation 
        op = operation
        total = num_list[k][0] # start with the first number
        num_index = 1
        operation = operation + 1
        # continue until we process all operations or go over the result
        while (num_index < len(num_list[k])) and (total < result[k]):
            current_op = op % 3
            op = op // 3
            if current_op == 0:
                total *= num_list[k][num_index]
            elif current_op == 1:
                total += num_list[k][num_index]
            else:
                # concatenation
                #print("concat")
                num_index = num_index+1-1 # move ahead one more because we used two number

            num_index = num_index +1
        
        if (total == result[k]):
            result_set.add(result[k])
            #print(num_list[k], result[k])

# total up the result set
sum = 0
for x in result_set:
    sum = sum + x

print(sum)

    
        
    