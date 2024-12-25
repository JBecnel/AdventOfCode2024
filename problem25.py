


def obtain_input(file_name):
    with  open(file_name, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    
    index = 0
    
    keys = []
    locks = []
    while index < len(lines):
        parse_schematics(lines[index:index+7], keys, locks)
        index = index + 8
        
    return keys, locks
        
def get_combo(scheme):
    combo = [0]*5
    for r in range(len(scheme)):
        for c in range(len(scheme[r])):
            if scheme[r][c] == "#":
                combo[c] = combo[c] + 1
    return combo
    
def parse_schematics(scheme, keys, locks):
    hash = "#" * 5
    dots = "." *  5
    if scheme[0] == hash and scheme[-1] == dots:
        locks.append(get_combo(scheme[1:len(scheme)-1]))
    
    if scheme[0] == dots and scheme[-1] == hash:
        keys.append(get_combo(scheme[1:len(scheme)-1]))
    
def fits(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > 5:
            return False
        
    return True

def main():
    file_name = "puzzle25.dat"
    #file_name = "puzzle25_sample.dat"
    keys, locks = obtain_input(file_name)
    
    #print(keys, locks)

    count = 0
    for key in keys:
        for lock in locks:
            if fits(key, lock):
                count = count + 1
    
    print(count)
if __name__ == "__main__":
    main()