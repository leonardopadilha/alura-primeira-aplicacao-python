# Escreva uma funçaõ que gere a tabuada de um número inteiro de 1 a 10, de acordo com a pessoa usuária.

num = int(input("Digite um número desejado: "))
print(f'Tabuada do {num}')
for i in range(11):
  print(f'{num} x {i} = {num * i}')