dBug = False
blinks = 75

def clean(str):
    index = 0
    while str[index] == '0' and index < len(str)-1:
        index = index + 1

    return str[index:len(str)]


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append('1')
        elif len(stone) % 2 == 0:
            size = len(stone) // 2
            new_stones.append(stone[0:size])
            stone2 = stone[size:len(stone)]
            stone2 = clean(stone2)
            new_stones.append(stone2)
        else:
            value = int(stone)
            value = value * 2024
            new_stones.append(str(value))

    return new_stones



def process_stones(stones):
    update_stones = stones.copy()
    for i in range(blinks):
        if dBug:
            print('updated stones: ', update_stones)
        update_stones = blink(update_stones)

    return len(update_stones)


def main():
    filename = 'puzzle11_sample.dat'
    with open(filename, 'r') as f:
        for line in f:
            row = [x for x in line.split()]
            if dBug:
                print("init row", row)
            print(process_stones(row))
        

if __name__ == '__main__':
    main()