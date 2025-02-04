# Escreva um código que lê a lista abaixo e faça:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

# A leitura do tamanho da lista
print(f'Tamano da lista: {len(lista)} itens')
# A leitura do maior e menor valor
print(f'O maior número da lista é: {max(lista)} e o menor é: {min(lista)}')
maior_numero = 0
menor_numero = len(lista)

for i in lista:
  if i > maior_numero:
    maior_numero = i
  
  if i < menor_numero:
    menor_numero = i
print(f'O maior número com for é: {maior_numero} e o menor número é: {menor_numero}')

# A soma do valores da lista 
soma = 0
for i in lista:
  soma += i
print(f'O total da soma com for é: {soma} e com função built-in é {sum(lista)}')