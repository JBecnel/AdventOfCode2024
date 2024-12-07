# Determine if the update is valid
# based on given ordering.
# We also correct the out of order update
# Basically we are performing a bubble sort but 
# instead of a numerical ordering, we use the given ordering
def valid_update(update, order):
    valid = True
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in order:
                if update[i] in order[update[j]]:
                    temp = update[i]
                    update[i] = update[j]
                    update[j] = temp
                    valid = False
            
    return valid


# grab the input from the file
list1 = []
list2 = []
updates = []
file_name = 'puzzle5_sample.dat'
file_name = 'puzzle5.dat'
with open(file_name, 'r') as puzzle1_file:
    for line in puzzle1_file:
        if "|" in line:
            nums = line.split('|')
            list1.append(int(nums[0].strip()))
            list2.append(int(nums[1].strip()))
        else:
            if len(line.strip()) > 0:
                numbers = line.strip().split(',')
                updates.append([int(num) for num in numbers])


# create a dictionary where the key is a page number
# and the value is a list containing all pages that must come after
order = { }
for i in range(len(list1)):
    if list1[i] in order:
        order[list1[i]].append(list2[i])
    else:
        order[list1[i]] = [list2[i]]

# find the sum of the middle numbers of all updates that are not valid
sum = 0
for update in updates:
   if not valid_update(update, order):
       sum = sum + int(update[len(update)//2])

print(sum)
