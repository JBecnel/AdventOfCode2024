


def secret(num,iter=10):
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

    return num 
        
if __name__ == '__main__':
    nums= [1,10,100,2024]
    for num in nums:
        secret(num,2000)
        
    total_sum = 0
    with open('puzzle22.dat', 'r') as file:
        for line in file:
            num = int(line.strip())
            total_sum += secret(num, 2000)
    
    print(f'Total sum: {total_sum}')