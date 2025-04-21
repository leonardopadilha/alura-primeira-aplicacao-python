# raise NomeDoErro("Mensagem desejada")

def media(lista: list = [0]) -> float:
  if len(lista) > 4:
    raise ValueError("A lista não pode possuir mais de 4 notas")
  return sum(lista) / len(lista)


try:
  notas = [6, 7, 8, 9]
  resultado = media(notas)
except TypeError:
  print("Não foi possível calcular a média do(a) estudante. Só são aceitos valores numéricos!")
except ValueError as e:
  print(e)
else:
  print(resultado)
finally:
  print("A consulta foi encerrada!")