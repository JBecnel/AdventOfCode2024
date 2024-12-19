dBug = False # flag to display debugging info

# get the input from the file
def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    tokens = lines[0].split(",")   # set of all wall locations
    tokens = [token.strip() for token in tokens]
    
    lines.pop(0)
    lines.pop(0)

    return tokens, lines

# count the possible constructions
# of the given pattern from the list of tokens
# count is a Hash Map to keep track of the
# of current count of a pattern
def num_construct(pattern, tokens, seen):

    if pattern in seen:
        return seen[pattern]  # return the value if already known
    else:
        seen[pattern] = 0     # initialize the value if not
    
    count = seen[pattern]  # counts the number of ways to form the pattern
    for t in tokens:
        if t == pattern  or len(pattern) == 0:
            count = count + 1            
        else:
           if pattern.startswith(t):               
               count = count + num_construct(pattern[len(t):], tokens, seen)
    
    seen[pattern] = count 
    return count

def main():
    #file_name = "puzzle19_sample.dat"
    file_name = "puzzle19.dat"
    tokens, patterns = obtain_input(file_name)

    if dBug:
        print("tokens ", tokens)
        print("pattern ", patterns)
    
    count = { }
    for p in patterns:
        num_construct(p, tokens, count)

    if dBug:
        print(count)
    
    # sum up the total pattern combos
    sum = 0
    for p in patterns:
        sum = sum = sum + count[p]
    print(sum)

if __name__ == "__main__":
    main()