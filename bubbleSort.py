def bubbleSort(array):
  for i in range(0, len(array)):
      for j in range(0, len(array)):
          if(array[j] > array[i]):
              aux = array[i];
              array[i] = array[j];
              array[j] = aux;

array = [15,7,8,23,4,1,54,2];
array1 = [99, -3, 10, 25, 44, 1, 83];
array2 = [999, 345, -1, 22, -349, 4];
bubbleSort(array);
bubbleSort(array1);
bubbleSort(array2);
print(array);
print(array1);
print(array2);