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
    if (len(integers)) < 2:
      return pairs

    integers.sort()

    count = 0

    i = 0

    # test all possible pairs,; check their sums
    while (i < len(integers) - 1):

      count += 1

      if integers[i] > target:
        break

      j = 1

      while (j < len(integers)):
        #print("comparing: {} and {}".format(integers[i], integers[j]))

        count += 1

        int_sum = integers[i] + integers[j]

        if int_sum > target:
          break

        if int_sum == target:
          #print("found {} and {}".format(integers[i], integers[j]))
          pairs.append([integers[i], integers[j]])
          integers.remove(integers[i])
          integers.remove(integers[j-1])
          i = i - 1
          j = j - 1
          break

        j += 1
      i += 1

    print(pairs)
    print("iterations: {}".format(count))
    print("pairs: {}".format(len(pairs)))

# test cases
Pairs(list(range(0, 1000011)), 5500)
Pairs(list(range(-10000, 10001)), 5)
Pairs(list(range(0, 11)), 5)
Pairs(list(range(-10, 1)), -5)
