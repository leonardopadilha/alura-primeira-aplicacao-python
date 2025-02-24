from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
  
  restaurantes = []
  
  def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria.upper()
    self._ativo = False
    self._avaliacao = []
    self._cardapio = []
    Restaurante.restaurantes.append(self)

  def __str__(self):
    return f'{self._nome} | {self._categoria}'

  @classmethod 
  def listar_restaurantes(cls):
    dados_restaurante = ['Nome do restaurante', 'Categoria', 'Avaliação', 'Status']
    print(f'{dados_restaurante[0].ljust(25)} | {dados_restaurante[1].ljust(25)} | {dados_restaurante[2].ljust(25)} |{dados_restaurante[3]}')
    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

  @property # Modificando como o atributo será lido
  def ativo(self):
    return '☑' if self._ativo else '☐'
  
  def alternar_estado(self):
    self._ativo = not self._ativo

  def receber_avaliacao(self, cliente, nota):
    if 0 < nota <= 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)

  @property
  def media_avaliacoes(self):
    if not self._avaliacao:
      return '-'
    return round(sum(avaliacao._nota for avaliacao in self._avaliacao) / len(self._avaliacao), 1)
  
  def adicionar_no_cardapio(self, item):
    if isinstance(item, ItemCardapio):
      self._cardapio.append(item)

  @property
  def exibir_cardapio(self):
    print(f"Cardápio do restaurante {self._nome}\n")
    for i,item in enumerate(self._cardapio,start=1):
      if hasattr(item, '_descricao'):
        mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item._descricao}"
        print(mensagem_prato)
      else:
        mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item._tamanho}"
        print(mensagem_bebida)