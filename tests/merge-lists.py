def merge_lists(list1, list2):
  merged_list = []
  counter = 0

  while counter < len(list1) and counter < len(list2):
    merged_list.append(list1[counter])
    merged_list.append(list2[counter])

    counter += 1

  print(merged_list)

l1 = [1,2,3,4]
l2 = ['a','b','c','d','e']

merge_lists(l1, l2)
