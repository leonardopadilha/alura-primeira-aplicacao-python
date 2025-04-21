nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

# [resultado_if if cond else resultado_else for item in lista]

situacao = ["Aprovado(a)" if media >= 6 else "Reprovado(a)" for media in medias]
#print(situacao)

#cadastro = [x for x in [nomes, notas, medias, situacao]]
#print(cadastro)

lista_completa = [nomes, notas, medias, situacao]
#print(lista_completa)

coluna = ["Notas", "Media Final", "Situacao"]

# Dict comprehension
# { chave: valor for item in lista }
cadastro = {coluna[i]: lista_completa[i + 1] for i in range(len(coluna))}
#print(cadastro)

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
print(cadastro)

