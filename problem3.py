import re

file_name = "puzzle3_prob.dat"
#file_name = 'puzzle3_sample.dat'

# regex pattern for mul(<int>,<int>)
pattern = "mul\([0-9]+,[0-9]+\)"

with open(file_name, 'r') as puzzle_file:
    sum = 0  # tracks the sum
    for line in puzzle_file:
        matches = re.findall(pattern, line)  # find all the multiple instructions
        #print(matches)      
        for match in matches: # pull the numbers out, multiply then and add to the sum
            nums = re.findall(r"\d+", match)
            sum = sum + int(nums[0]) * int(nums[1])

print(sum)
  
       
