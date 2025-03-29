# Criando a função que recebe a lista de palavras
def avalia_texto(texto: list):
  for palavra in texto:
    if ',' in palavra or '.' in palavra or '!' in palavra or '?' in palavra:
      raise ValueError(f'O texto apresenta pontuações na palavra {palavra}')
  return "Texto já tratado" # retornando a verificação se não lançada

try:
  texto = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
          'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
          'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

  resultado = avalia_texto(texto)

except ValueError as e:
  print(e)
else:
  print(resultado)