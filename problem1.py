# read the two arrays from puzzle1.dat
list1 = []
list2 = []
with open('puzzle1_prob.dat', 'r') as puzzle1_file:
    for line in puzzle1_file:
        nums = line.strip().split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

# sort list1 and list2
list1.sort()
list2.sort()

import numpy as np
l1 = np.array(list1)
l2 = np.array(list2)

# compute the l1 distance between l1 and l2
distance = np.sum(np.abs(l1 - l2))
print(distance)