
def somar_dois_numeros(num1, num2):
  return num1 + num2
  
def subtrair_dois_Numeros(num1, num2):
  return num1 - num2
  
def multiplicar_dois_numeros(num1, num2):
  return num1 * num2
  
def dividir_dois_numeros(num1, num2):
  return num1 / num2
  
def calcular():
  print(''' Escolha uma opção:
        1. Somar
        2. Subtrair
        3. Multiplicar
        4. Dividir
        ''')
  menu = int(input("Opcao desejada: "))
  num1 = int(input("Informe o primeiro número: "))
  num2 = int(input("Informe o segundo número: "))

  if menu == 1:
    resultado = somar_dois_numeros(num1, num2)
  elif menu == 2:
    resultado = subtrair_dois_Numeros(num1, num2)
  elif menu == 3:
    resultado = multiplicar_dois_numeros(num1, num2)
  elif menu == 4:
    resultado = dividir_dois_numeros(num1, num2)
  else:
    print("Digite um número válido para operação")

  print(f"O resultado da operação é: {int(resultado)}")


calcular()