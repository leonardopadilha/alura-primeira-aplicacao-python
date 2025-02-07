notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

notas_atualizadas = map(lambda x: x + qualitativo, notas)
print(list(notas_atualizadas))

temp_celsius = [0, 25, 37, 78, 100]
temp_fahrenheit = list(map(lambda x: (x * 9/5 + 32), temp_celsius))
print(temp_fahrenheit)