

# computes the secret in number in accordance with the problem
def secret(num,iter=10):
    prev_digit = num % 10
    num_list = [ ]
    for i in range(iter):
        # step 1
        result = num << 6
        num = result ^ num 
        num = num % 16777216

        # step 2
        div_32 = num >> 5
        num = div_32 ^ num
        num = num % 16777216

        # step 3
        shift_11 = num << 11
        num = shift_11 ^ num
        num = num % 16777216
        
        digit = num % 10
        diff = digit - prev_digit
        prev_digit = digit
        
        num_list.append((digit, diff))
        
    return num_list

def add_to_quad_dist(dig_diff_list):
    # for each quad sequence, add the quad sequence as a key
    # and the digit as the value
    quad = (dig_diff_list[0][1], dig_diff_list[1][1], dig_diff_list[2][1], dig_diff_list[3][1])
    
    quad_dist = { quad : dig_diff_list[3][0] }
    for i in range(4, len(dig_diff_list)):
        quad = (quad[1], quad[2], quad[3], dig_diff_list[i][1])
        if quad not in quad_dist:
            quad_dist[quad] = dig_diff_list[i][0]
        #elif quad_dist[quad] < dig_diff_list[i][0]:
        #    quad_dist[quad] = dig_diff_list[i][0]
    
    return quad_dist 

# this functions merges to "quad" dictionary 
# and finds the sum of the values
def merge(quad_dist, quad):
    for key in quad:
        if key not in quad_dist:
            quad_dist[key] = quad[key]
        else:
            quad_dist[key] += quad[key]
          
if __name__ == '__main__':
    #nums= [1,10,100,2024]
    #nums= [123]
    #nums = [1,2,3,2024]
    nums = []
    with open('puzzle22.dat', 'r') as file:
        for line in file:
            nums.append(int(line.strip()))
            
    
   

    quad_dist = {}
    for num in nums:
        dig_diff_list = secret(num,2000)
        #print(dig_diff_list)
        quad = add_to_quad_dist(dig_diff_list)
        #print(quad)
        merge(quad_dist, quad)
    
    # find which quad sequence has the maximum value
    max_sum = 0
    max_key = None
    for key in quad_dist:
        sum_val = quad_dist[key]
        
        if sum_val > max_sum:
            max_sum = sum_val
            max_key = key

        
    print(max_sum)
    print(max_key)
   