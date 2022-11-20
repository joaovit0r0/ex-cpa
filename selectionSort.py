def selectionSort(array):

  # Percorre todo o array
  for posAtual in range(0, (len(array) -1)):
    # Salva a posição do menor elemento, inicialmente a posAtual
    posMenor = posAtual;
    
    # Percorre o array da (posAtual + 1), até o final
    # Não precisa percorrer do inicio pois já está garantida a ordenação do laços anteriores do codigo
    for posNovoMenor in range((posAtual + 1), len(array)):
      # Procura o menor elemento no array, coparando o elemento atualmente menor na posMenor com os demais na posNovoMenor
      if(array[posNovoMenor] < array[posMenor]):
        # Sé encontrar salva a posição do novo menor elemento na posMenor
        posMenor = posNovoMenor;
    
    # Sé o valor do arrey na posAtual for diferente da posMenor, há um elemento menor que o elemento da posAtual
    if(array[posAtual] != array[posMenor]):
      # Troca os elementos do verto de posição
      aux = array[posAtual];
      array[posAtual] = array[posMenor];
      array[posMenor] = aux;

  return array;

array = [15,7,8,23,4,1,54,2];
array1 = [99, -3, 10, 25, 44, 1, 83];
array2 = [999, 345, -1, 22, -349, 4];
selectionSort(array);
selectionSort(array1);
selectionSort(array2);
print(array);
print(array1);
print(array2);