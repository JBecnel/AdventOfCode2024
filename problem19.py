dBug = True  # flag to display debugging info

# get the input from the file
def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    tokens = lines[0].split(",")   
    tokens = [token.strip() for token in tokens]
    
    lines.pop(0)
    lines.pop(0)

    return tokens, lines

# flag the possible constructions
# of the given pattern from the list of tokens
# seen is a Hash Map to keep track of the
# of previously seen patterns
def can_construct(pattern, tokens, seen):

    # if already known return
    if pattern in seen:
        return seen[pattern]
    
    # see if each token can be used to make the pattern
    for t in tokens:
        if t == pattern  or len(pattern) == 0:
            seen[pattern] = True
            return True 
        else:
           if pattern.startswith(t):               
               # recursively check if the rest of the pattern
               # can be constructed via the tokens
               if can_construct(pattern[len(t):], tokens, seen):
                   seen[pattern] = True
                   return True
    
    # if we arrived here, we cannot make the pattern, return false
    seen[pattern] = False
    return False

def main():
    file_name = "puzzle19_sample.dat"
    file_name = "puzzle19.dat"
    tokens, pattern = obtain_input(file_name)

    if dBug:
        print("tokens ", tokens)
        print("pattern ", pattern)

    count = 0
    seen = { }
    for p in pattern:
        if can_construct(p, tokens, seen):
            count = count + 1

    if dBug:
        print(seen)
    
    print(count)

if __name__ == "__main__":
    main()