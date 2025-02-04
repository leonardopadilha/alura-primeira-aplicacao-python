# Crie uma lista dos quadrados dos númeoros da seguinte lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def numero_ao_quadrado(num):
  numeros_quadrado = []
  for i in num:
    numeros_quadrado.append(i**2)
  return numeros_quadrado

print(numero_ao_quadrado(numeros))

numero_quadro_lambda = list(map(lambda x: (x ** 2), numeros))
print(numero_quadro_lambda)