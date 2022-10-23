def shellSort(input_list):
   gap = len(input_list) // 2
   while gap > 0:
      for i in range(gap, len(input_list)):
         temp = input_list[i]
         j = i
# Sort the sub list for this gap
   while j >= gap and input_list[j - gap] > temp:
      input_list[j] = input_list[j - gap]
      j = j-gap
      input_list[j] = temp
# Reduce the gap for the next element
   gap = gap//2
list = [83,99,12,24,36,19,8,3,37]
shellSort(list)
print(list)
