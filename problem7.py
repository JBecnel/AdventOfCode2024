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
    # for k from 0 to 2^n-1
    num_operations = len(num_list[k])-1
    # for each binary number  from 0 to 2^(n-1)-1
    # calculate the sum of the numbers in num_list[i] that correspond to the binary digits in i
    # and append the sum to the result list if the sum is equal to the result[i]
    for i in range(1 << num_operations):
        total = num_list[k][0] 
        for j in range(1, num_operations+1):  # j traverses the number of bits in i
            if i & (1 << (j-1)):   # when i has a 1 bit, we add
                total += num_list[k][j]
            else:                   # when i has a 0 bit we multiply
                total *= num_list[k][j]
            #print(f'For result[{k}] = {result[k]}, the result of {num_list[k]} is {total} for i = {i} and j = {j}.')
        if (total == result[k]):
            result_set.add(result[k])
            #print(num_list[k], result[k])

# total up the result set
sum = 0
for x in result_set:
    sum = sum + x

print(sum)

    
        
    