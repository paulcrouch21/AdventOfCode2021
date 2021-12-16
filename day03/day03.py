import sys
import collections

def main():
    #create an array of the input (each line is an element of the array)
    with open(sys.argv[1]) as myFile:
        input = myFile.readlines()
        input = [line.rstrip() for line in input]

    #create an array for each bit with each index being an array representing how many zeroes and how many ones
    #counters = [[0, 0]] * len(input[0])
    pivot = [[x[i] for x in input] for i in range(len(input[0]))]
    colls = [collections.Counter(x) for x in pivot]

    for i in colls:
        print(i)

    '''
    #find out how many 0's and 1's in each bit
    for i in range(len(input)):
        for j in range(len(input[i])):
            if int(input[i][j]) == 0:
                #increase counter for zero by 1
                counters[j][0] += 1
            elif int(input[i][j]) == 1:
                #increase counter for one by 1
                counters[j][1] += 1
            #print(counters)

    print(counters)
    '''

if __name__ == '__main__':
    main()