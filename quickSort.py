def partition(array, low, high):

  pivot = array[high]

  i = low - 1

  for j in range(low, high):
    
    if array[j] <= pivot:
    
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quickSort(array, low, high):
  if low < high:

    pi = partition(array, low, high);

    quickSort(array, low, pi - 1);

    quickSort(array, pi + 1, high);


array = [15,7,8,23,4,1,54,2];
size = len(array);
quickSort(array, 0, size - 1)

array1 = [99, -3, 10, 25, 44, 1, 83];
size = len(array1);
quickSort(array1, 0, size - 1);

array2 = [999, 345, -1, 22, -349, 4];
size = len(array2);
quickSort(array2, 0, size - 1);
print(array);
print(array1);
print(array2);
