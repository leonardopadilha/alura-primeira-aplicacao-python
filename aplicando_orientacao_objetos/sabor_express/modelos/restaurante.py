class Restaurante:
  
  restaurantes = []
  
  def __init__(self, nome, categoria):
    self.nome = nome
    self.categoria = categoria
    self.ativo = False
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f'{self.nome} | {self.categoria}'

  def listar_restaurantes():
    for restaurante in Restaurante.restaurantes:
      print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

print(vars(restaurante_praca)) # Exibe as informações da classe como um dicionário
# print(dir(restaurante_praca)) # Exibe os métodos disponíveis para aquela classe

print(restaurante_praca)

print()

Restaurante.listar_restaurantes()