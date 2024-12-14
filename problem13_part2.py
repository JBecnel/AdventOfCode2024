import numpy as np
import re 
def parse_input():
    # Read the input file
    file_path = "puzzle13_sample1.dat"
    file_path = "puzzle13.dat"
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]

    A_button = []
    B_button = []
    Prize = [ ]
    for i in range(0, len(lines)):
        numbers = re.findall(r"-?\d+", lines[i])
        numbers = list(map(int, numbers))  # Convert to integer
        if i % 4 == 0:
            A_button.append((numbers[0], numbers[1]))
        elif i % 4 == 1:
            B_button.append((numbers[0], numbers[1]))
        elif i % 4 == 2:
            Prize.append((numbers[0]+10000000000000, numbers[1]+10000000000000))
        
    return A_button, B_button, Prize

def solve(coef1, coef2, b):
    
    # Coefficient matrix A
    A = np.array([[coef1[0], coef2[0]] ,
                  [coef1[1], coef2[1]]])

    # Constant matrix B
    B = np.array([b[0], b[1]])

    # Solve for x (the variables)
    x = np.linalg.solve(A, B)

    return x


def main():
    A, B, prize = parse_input()
    tokens = 0
    for i in range(0, len(A)):
        solution = solve(A[i], B[i], prize[i])
        print(solution)
        if np.linalg.norm(solution - np.round(solution,decimals=0)) < 0.01:
            tokens += solution[0] * 3 + solution[1]
            print(tokens)
    print("Tokens collected: ", tokens)

    
    
if __name__ == '__main__':
    main()