class Livro:
  def __init__(self, titulo, autor, ano_publicacao):
    self.titulo = titulo
    self.autor = autor
    self.ano_publicacao = ano_publicacao
    self.disponivel = True

  def __str__(self):
    return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de publicação: {self.ano_publicacao}"
  
  def emprestar(self):
    self.disponivel = False

  @staticmethod
  def verificar_disponibilidade(ano):
    livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
    return livros_disponiveis
  

livro1 = Livro("Aprendendo Python", "John Doe", 2022)
livro2 = Livro("Python in Practice", "Emily Coder", 2021)

Livro.livros = [livro1, livro2]

print(livro1)

""" ano_especifico = 2022
livros_disponiveis = Livro.verificar_disponibilidade(ano_especifico)
print(f"{livros_disponiveis}") """