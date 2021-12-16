import sys

def main():
    with open(sys.argv[1]) as myFile:
        lines = myFile.readlines()
        lines = [line.rstrip().split(' ') for line in lines]

    #part 1
    horizontal = 0
    depth = 0

    for i in range(len(lines)):
        if lines[i][0] == 'forward':
            #increase horizontal
            horizontal += int(lines[i][1])
        elif lines[i][0] == 'down':
            #increase depth
            depth += int(lines[i][1])
        elif lines[i][0] == 'up':
            #decrease depth
            depth -= int(lines[i][1])

    print(f'Horizontal: {horizontal}, Depth: {depth}')
    print(f'The answer is {horizontal * depth}')

    #part 2
    horizontal = 0
    depth = 0
    aim = 0

    for i in range(len(lines)):
        if lines[i][0] == 'forward':
            #increase horizontal
            horizontal += int(lines[i][1])
            depth = depth + (aim * int(lines[i][1]))
        elif lines[i][0] == 'down':
            #increase depth
            aim += int(lines[i][1])
        elif lines[i][0] == 'up':
            #decrease depth
            aim -= int(lines[i][1])

    print(f'Horizontal: {horizontal}, Depth: {depth}, Aim: {aim}')
    print(f'The answer is {horizontal * depth}')

if __name__ == '__main__':
    main()