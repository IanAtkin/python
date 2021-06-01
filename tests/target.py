#!/usr/bin/python3.6

# write a function with the following input: an array of integers and a number 'target'
# find all the pairs that sum equals to the input number 'target'
# output is a list of pairs (number_a, number_b)

# e.g input: [1,3,9,-5,-2,0,100,-25], -2
# e.g output [(3,-5), (-2,0)]
# assume the input array has no duplicates

class Pairs:

  def __init__(self, integers, target):
    self.findPairs(integers, target)

  def findPairs(self, integers, target):
    pairs = []
    length = len(integers)

    # test all possible pairs,; check their sums
    for i in range(0, length):
      for j in range(i + 1, length):
        if integers[i] + integers[j] == target:
          pairs.append([integers[i], integers[j]])

    print(pairs)

# test cases
Pairs([1, 2, -3, 4, 5, 6, -7, 8, 9, 10], -10)
Pairs([1, 2, -3, -4, 5, -6, 7, 8, 9, -10], 17)
Pairs([-7, -5, -3, -1, 0, 4, 8, 12, 14, 16], -3)
Pairs([11, 9, 0, 14, 23], 23)
Pairs([34, 62, 57, 39, 91, 3, 59, 99, 38, 78, 45, 54, 89, 24, 22, 33, 6, 26, 70, 55, 44, 1, 4, 47, 15, 79, 98, 41, 61, 69, 73, 28, 52, 13, 92, 51, 58, 87, 75, 40, 49, 19, 71, 83, 37, 12, 50, 86, 23, 27, 21, 18, 81, 25, 8, 66, 60, 35, 88, 82, 43, 5, 80], 123)