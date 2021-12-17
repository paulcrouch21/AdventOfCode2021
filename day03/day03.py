import sys
import collections

def main():
     #create an array of the input (each line is an element of the array)
     with open(sys.argv[1]) as myFile:
          input = myFile.readlines()
          input = [line.rstrip() for line in input]

     numberOfLines = len(input)
     counters = [[0, 0] for _ in range(len(input[0]))]

     #determines the most common bit in each position
     j = 0
     while j < len(input[0]):
          i = 0
          while i < numberOfLines:
               if int(input[i][j]) == 0:
                    counters[j][0] += 1
               elif int(input[i][j]) == 1:
                    counters[j][1] += 1
               i += 1
          j += 1

if __name__ == '__main__':
     main()