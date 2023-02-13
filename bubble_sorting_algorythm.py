def bubble_sorting(list_of_elements):

  length_list = len(list_of_elements)

  while length_list > 1:
    zamien = False
    for index in range(length_list - 1):

      if list_of_elements[index] > list_of_elements[index + 1]:
        list_of_elements[index], list_of_elements[index + 1] = list_of_elements[index + 1], list_of_elements[index]
        zamien = True

    length_list -= 1
    if zamien == False:
      break

  return list_of_elements

print(bubble_sorting([1,2,5,3,1,7,9,1,12,83,1,5,3,2]))
print(bubble_sorting([]))
print(bubble_sorting([1,1,1,1,1,1,1,2,1,1,1]))
print(bubble_sorting([2,2,2,2]))
print(bubble_sorting([1,2]))
print(bubble_sorting([2, 1]))
