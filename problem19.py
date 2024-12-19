dBug = True


def obtain_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    tokens = lines[0].split(",")   # set of all wall locations
    
    lines.pop(0)
    lines.pop(0)

    

    return tokens, lines

def main():
    file_name = "puzzle19_sample.dat"
    tokens, pattern = obtain_input(file_name)

    if dBug:
        print("tokens ", tokens)
        print("pattern ", pattern)

if __name__ == "__main__":
    main()