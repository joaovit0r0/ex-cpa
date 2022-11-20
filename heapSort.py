def heapSort(array):
  tamanho = len(array);
  pivo = tamanho / 2;
  t = 0;
  while(True):
    if pivo > 0:
      pivo -= 1;
      t = array[int(pivo)];
    else:
      tamanho-= 1;
      if(tamanho<=0):
        return;
      t = array[int(tamanho)];
      array[tamanho] = array[0];
    pai = pivo;
    filho = ((pivo * 2) + 1);
    while(filho < tamanho):
      if ((filho + 1 < tamanho) and (array[int(filho + 1)] > array[int(filho)])):
        filho += 1;
      if(array[int(filho)]>t):
        array[int(pai)] = array[int(filho)]
        pai = filho;
        filho = pai * 2 + 1;
      else:
        break;
    array[int(pai)] = t;

array = [15,7,8,23,4,1,54,2];
array1 = [99, -3, 10, 25, 44, 1, 83];
array2 = [999, 345, -1, 22, -349, 4];
heapSort(array);
heapSort(array1);
heapSort(array2);
print(array);
print(array1);
print(array2);