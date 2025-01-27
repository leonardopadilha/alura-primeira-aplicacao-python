class Restaurante:
  
  restaurantes = []
  
  def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria.upper()
    self._ativo = False
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f'{self._nome} | {self._categoria}'

  @classmethod 
  def listar_restaurantes(cls):
    dados_restaurante = ['Nome do restaurante', 'Categoria', 'Status']
    print(f'{dados_restaurante[0].ljust(25)} | {dados_restaurante[1].ljust(25)} | {dados_restaurante[2]}')
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

  @property # Modificando como o atributo será lido
  def ativo(self):
    return '☑' if self._ativo else '☐'
  
  def alternar_estado(self):
    self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

print(vars(restaurante_praca)) # Exibe as informações da classe como um dicionário
# print(dir(restaurante_praca)) # Exibe os métodos disponíveis para aquela classe

#print(restaurante_praca)

print()

Restaurante.listar_restaurantes()