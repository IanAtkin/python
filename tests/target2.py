#!/usr/bin/python3.6

# write a function with the following input: an array of integers and a number 'target'
# find all the pairs that sum equals to the input number 'target'
# output is a list of pairs (number_a, number_b)

# e.g input: [1,3,9,-5,-2,0,100,-25], -2
# e.g output [(3,-5), (-2,0)]
# assume the input array has no duplicates

# slight iteration of previous function that sorts the list and then ignores values larger than the target sum
# this optimization assumes large data sets since the sorting reduces the effectiveness on smaller data sets to some degree
# tested with a list of 10,000 values

class Pairs:

  def __init__(self, integers, target):
    self.findPairs(integers, target)

  def findPairs(self, integers, target):
    pairs = []
    length = len(integers)

    integers.sort()

    # test all possible pairs,; check their sums
    for i in range(0, length):

      # break here if number_a is larger than the target sum
      if integers[i] > target:
        break

      for j in range(i + 1, length):

        int_sum = integers[i] + integers[j]

        # break here if number_a + number_b is larger than the target sum
        if int_sum > target:
          break

        if int_sum == target:
          pairs.append([integers[i], integers[j]])

    print(pairs)

# test cases
Pairs([0, 1, 2, 3, 4], 2)
Pairs([34, 62, 57, 39, 91, 3, 59, 99, 38, 78, 45, 54, 89, 24, 22, 33, 6, 26, 70, 55, 44, 1, 4, 47, 15, 79, 98, 41, 61, 69, 73, 28, 52, 13, 92, 51, 58, 87, 75, 40, 49, 19, 71, 83, 37, 12, 50, 86, 23, 27, 21, 18, 81, 25, 8, 66, 60, 35, 88, 82, 43, 5, 80], 56)
Pairs([15, 482, 864, -620, 477, 561, 39, 917, -532, -941, 993, -791, -796, 14, -808, 80, 405, -982, 834, 846, 564, -88, -938, 761, 804, -759, 139, -753, -59, -546, -948, 132, -612, -148, -393, -350, -557, -379, -80, 980, -319, 558, -552, 642, -33, -293, -571, 244, -942, -528, 315, -1, 984, 699, 643, -955, 715, 330, 711, 571, -220, 521, 923, -871, 950, -407, 935, 735, -478, 876, 25, 888, 456, 486, -114, 615, -956, 386, 334, -455, -223, -104, 288, 108, 829, -202, 165, 372, -996, -523, -725, 897, -136, 425, 210], 142)