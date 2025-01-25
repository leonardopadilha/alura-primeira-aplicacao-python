import os

restaurantes = [{'nome': 'Macarrao do Zé', 'categoria': 'Restaurante', 'ativo': False}, 
                {'nome': 'Churras do Zé', 'categoria': 'Rodízio', 'ativo': True}, 
                {'nome': 'Sorvete', 'categoria': 'Sorveteria', 'ativo': False}]

def finalizar_app():
  exibir_subtitulo('Encerrando...')

def exibir_nome_do_programa():
  print(""" 
  ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
  ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
  ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
  ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
  ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
  """)

def exibir_opcoes():
  print("""1. Cadastrar restaurante 
  2. Listar restaurante 
  3. Ativar ou desativar restaurante 
  4. Sair
  """)

def voltar_ao_menu_principal():
  input('Digite uma tecla para voltar ao menu anterior ')
  main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
  print('Opção inválida. Por favor, tente novamente.\n')
  voltar_ao_menu_principal()
 
def cadastrar_novo_restaurante():
  exibir_subtitulo('Cadastrar novo restaurante')
  nome_do_restaurante = input('Digite o nome do restaurante: ')

  categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
  dados_do_restaurante = { 'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False }
  restaurantes.append(dados_do_restaurante)
  print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!')
  voltar_ao_menu_principal()

def listar_restaurantes():
  exibir_subtitulo('Listando restaurantes')

  dados_restaurante = ['Nome do restaurante', 'Categoria', 'Status']
  print(f'{dados_restaurante[0].ljust(23)} | {dados_restaurante[1].ljust(20)} | {dados_restaurante[2]}')
  
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante['categoria']
    ativo = 'ativado' if restaurante['ativo'] else 'desativado'
    print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
  voltar_ao_menu_principal()


def alternar_estado_restaurante():
  exibir_subtitulo('Alternar estado do restaurante')
  nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if restaurante['nome'] == nome_restaurante:
      restaurante_encontrado = True
      restaurante['ativo'] = not restaurante['ativo'] # irá exibir o valor invertido nessa chave

      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)

  if not restaurante_encontrado:
      print(f'O restaurante {nome_restaurante} não foi encontrado')

  voltar_ao_menu_principal()

def escolher_opcao():
  try:
      opcao_escolhida = int(input('Escolha uma opcao: '))

      if opcao_escolhida == 1:
        cadastrar_novo_restaurante()
      elif opcao_escolhida == 2:
        listar_restaurantes()
      elif opcao_escolhida == 3:
        alternar_estado_restaurante()
      elif opcao_escolhida == 4:
        finalizar_app()
      else:
        opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcao()

if __name__ == '__main__':
  main()

