def merge(array, inicio, meio, fim):
  arrayAux = array.copy();
  iterador_inicio = inicio;
  iterador_meio = (meio + 1);
  iterador_ordenado = inicio;

  while(iterador_inicio <= meio and iterador_meio <= fim):

    if(arrayAux[iterador_inicio] <= arrayAux[iterador_meio]):
      array[iterador_ordenado] = arrayAux[iterador_inicio];
      iterador_inicio += 1;
    else:
      array[iterador_ordenado] = arrayAux[iterador_meio];
      iterador_meio += 1;

    iterador_ordenado += 1;

  while(iterador_inicio <= meio):
    array[iterador_ordenado] = arrayAux[iterador_inicio];
    iterador_inicio += 1;
    iterador_ordenado += 1;

  while(iterador_meio <= fim):
    array[iterador_ordenado] = arrayAux[iterador_meio];
    iterador_meio += 1;
    iterador_ordenado += 1;

  return array;


def mergeSortStarted(array, inicio, fim):
  if(inicio >= fim):
    return;
  else:
    meio = (inicio + fim) // 2;
    mergeSortStarted(array, inicio, meio);
    mergeSortStarted(array, (meio+1), fim);
    merge(array, inicio, meio, fim);
  
  return array;


def mergeSort(array):
  inicio = 0;
  fim = (len(array) -1);
  mergeSortStarted(array, inicio, fim);

  return array;

array = [15,7,8,23,4,1,54,2];
array1 = [99, -3, 10, 25, 44, 1, 83];
array2 = [999, 345, -1, 22, -349, 4];
mergeSort(array);
mergeSort(array1);
mergeSort(array2);
print(array);
print(array1);
print(array2);