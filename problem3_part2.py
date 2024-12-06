import re

file_name = "puzzle3_prob.dat"
#file_name = 'puzzle3_part2_sample.dat'


# grad the text form the file
text = ""
with open(file_name, 'r') as puzzle_file:
    sum = 0  # tracks the sum
    for line in puzzle_file:
        text = text + line.strip()


# do() and don't() pattern at the end of string
pieces = re.split(r"(do\(\)|don't\(\))", text)

#print(pieces)

compute = True # flag to to determine when to perform the computation
for txt in pieces:
    if txt.startswith("do()"): # when we see do(), start computing
        compute = True
    elif txt.startswith("don't()"):  # when we see don't(), stop computing
        compute = False
    elif compute: 
        # regex pattern for mul(<int>,<int>)
        pattern = "mul\([0-9]+,[0-9]+\)"
        matches = re.findall(pattern, txt)  # find all the multiple instructions
        for match in matches: # pull the numbers out, multiply then and add to the sum
            nums = re.findall(r"\d+", match)
            sum = sum + int(nums[0]) * int(nums[1])

print(sum)
  
       
