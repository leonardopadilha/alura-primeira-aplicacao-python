# Calcule a pontuação de um(a) skatista, é preciso eliminar a maior e a menor pontuação dentre
# dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:
# Nota da manobra: [media]

notas = []

n1 = float(input("Digite a 1ª nota: "))
notas.append(n1)

n2 = float(input("Digite a 2ª nota: "))
notas.append(n2)

n3 = float(input("Digite a 3ª nota: "))
notas.append(n3)

n4 = float(input("Digite a 4ª nota: "))
notas.append(n4)

n5 = float(input("Digite a 5ª nota: "))
notas.append(n5)

notas.remove(max(notas))
notas.remove(min(notas))

print(f'Nota da manobra: [{round(sum(notas) / len(notas), 2)}]')

