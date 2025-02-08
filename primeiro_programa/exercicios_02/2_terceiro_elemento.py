lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

terceiro_elemento = [lista_de_tuplas[i][2] for i in range(len(lista_de_tuplas))]
print(terceiro_elemento)

lista = []
for tupla in lista_de_tuplas:
  lista.append(tupla[2])
print(lista)