import sys

def main():
    #myFile = open(sys.argv[1], 'r')

    with open(sys.argv[1]) as myFile:
        lines = myFile.readlines()
        lines = [int(line.rstrip()) for line in lines]

    #part 1
    answer = compare(lines)

    print(f'How many measurements are larger than the previous measurement?\nAnswer: {answer}')

    #part 2
    myList = []
    i = 0
    while i + 2 < len(lines):
        sum = lines[i] + lines[i + 1] + lines[i + 2]
        myList.append(sum)
        i += 1

    answer = compare(myList)

    print(f'How many measurements are larger than the previous measurement with the new values?\nAnswer: {answer}')

def compare(values):
    i = 0
    counter = 0
    while i + 1 < len(values):
        if values[i] < values[i + 1]:
            counter += 1
        i += 1

    return counter


if __name__ == '__main__':
    main()