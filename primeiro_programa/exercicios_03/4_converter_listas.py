lista_1 = [4,6,7,9,10]
lista_2 = [-4,6,8,7,9]

def somar_listas(lista_1, lista_2):
  try:
    if len(lista_1) == len(lista_2):
      nova_lista = [(lista_1[i], lista_2[i], lista_1[i] + lista_2[i]) for i in range(len(lista_1))]
    else:
      raise IndexError('A quantidade de elementos em cada lista é diferente')
  except Exception as e:
    print(type(e), f'Erro: {e}')
  else: 
    return nova_lista

print(somar_listas(lista_1, lista_2))
    
  
