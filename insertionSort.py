def insertionSort(array):
  for j in range(1, len(array)):
    chave = array[j];
    i = j-1;

    while i >= 0 and array[i] > chave:
      array[i+1] = array[i];
      i = i-1
      
    array[i+1] = chave

  return array;

array = [15,7,8,23,4,1,54,2];
array1 = [99, -3, 10, 25, 44, 1, 83];
array2 = [999, 345, -1, 22, -349, 4];
insertionSort(array);
insertionSort(array1);
insertionSort(array2);
print(array);
print(array1);
print(array2);