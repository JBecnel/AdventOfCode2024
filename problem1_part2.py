import numpy as np

# read each column
list1 = np.loadtxt('puzzle1.dat', delimiter=" ", usecols=0, dtype=int) 


#print(list1)

list2 = np.loadtxt('puzzle1.dat', usecols=1, dtype=int) 
#print(list2)

# find the frequency of each element in column 1
nums1, freq1 = np.unique(list1, return_counts=True)

# find the frequency of each element in column 2
nums2, freq2 = np.unique(list2, return_counts=True)

#print(nums1, freq1, nums2, freq2)

# traverse nums1 array
sum = 0
for i in range(len(nums1)):
    # find the corresponding element in nums2 array
    idx = np.where(nums2 == nums1[i])[0]
    
    # if the number is in the second list
    if idx.size > 0:
        # update the similarity score
        # by taking the num times the freq in each list
        sum = sum + nums1[i] * freq1[i] * freq2[idx]
        

print(sum)
