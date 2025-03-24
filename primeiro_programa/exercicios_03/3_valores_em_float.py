def converter_valores_em_float(lista: list = [0]) -> list:
  listaFloat = []
  for i in lista:
    listaFloat.append(float(i))
  return listaFloat

# print(converterValoresEmFloat([1,2,3,4]))

# -----

def converter_valores_e_float_lambda(lista: list = [0]) -> list:
  return list(map(lambda x: float(x), lista))

# print(converterValoresEmFloatLambda([5,6,7,8,9]))

# ---- 
def converter_valores_em_float_comprehension(lista: list = [0]) -> list:
  return [float(i) for i in lista]

# print(converterValoresEmFloatComprehension([5,6,7,8,9]))

try:
  numeros = [5,6,7,8,9]
  resultado = converter_valores_em_float_comprehension(numeros)
except Exception as e:
  print(type(e), f'Erro: {e}')
else:
  print(resultado)
finally:
  print('Fim da execução da função')