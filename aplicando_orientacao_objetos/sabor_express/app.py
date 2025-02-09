
from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante('pizza express', 'Italiana')

#print(vars(restaurante_praca)) # Exibe as informações da classe como um dicionário
# print(dir(restaurante_praca)) # Exibe os métodos disponíveis para aquela classe

#print(restaurante_praca)

print()

# Restaurante.listar_restaurantes()

#restaurante_praca.receber_avaliacao('Leo', 10)
#restaurante_praca.receber_avaliacao('Luiz', 2)
#restaurante_praca.receber_avaliacao('Silva', 7)

bebida_suco = Bebida("Suco de Melancia", 5.0, 'grande')
prato_paozinho = Prato("Paozinho", 2.00, "O melhor pão da cidade")

bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
  # Restaurante.listar_restaurantes()
  restaurante_praca.exibir_cardapio

if __name__ == '__main__':
  main()