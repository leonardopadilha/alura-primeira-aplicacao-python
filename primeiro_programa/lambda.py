# Função lambda

n1 = float(input("Digite a 1ª nota do(a) estudante: "))
n2 = float(input("Digite a 2ª nota do(a) estudante: "))
n3 = float(input("Digite a 3ª nota do(a) estudante: "))

media_ponderada = lambda x,y,z : (x * 3 + y * 2 + z * 5)/10
media_estudante = media_ponderada(n1, n2, n3)
print(media_estudante)