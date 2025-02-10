meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesas = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

dicionario = { meses[i]: despesas[i] for i in range(len(meses))}
print(dicionario)


