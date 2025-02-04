# Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3
numeros = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
multiplos_por_tres = list(map(lambda x : x * 3, numeros))
print(multiplos_por_tres)

numero_por_tres = []
def multiplicar_por_tres(numeros: list) -> list:
  for i in range(len(numeros)):
    if numeros[i] % 3 == 0:
      numero_por_tres.append(numeros[i])
  return numero_por_tres

print(multiplicar_por_tres(numeros))
