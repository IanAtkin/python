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
    integers.sort()

    if len(integers) < 2:
      return pairs

    i = 0
    while i < len(integers):

      if integers[i] > -1:
        candidate = target - integers[i]
      else:
        candidate = abs(integers[i]) + target

      result = self.binarySearch(integers, 0, len(integers) - 1, candidate)

      if result != -1:
        pairs.append([integers[i], candidate])
        integers.remove(integers[i])

      i += 1

    print(pairs)
    print("pairs: {}".format(len(pairs)))

  def binarySearch(self, arr, l, r, x):

    if r >= l:
      offset = l + (r - l) // 2

      if arr[offset] == x:
        return offset
      elif arr[offset] > x:
        return self.binarySearch(arr, l, offset-1, x)
      else:
        return self.binarySearch(arr, offset+1, r, x)

    else:
      return -1

# test cases
Pairs(list(range(-10000, 10001)), -2)
Pairs(list(range(0, 11)), 5)
Pairs(list(range(-10, 11)), 5)
Pairs([1,3,9,-5,-2,0,100,-25], -2)
