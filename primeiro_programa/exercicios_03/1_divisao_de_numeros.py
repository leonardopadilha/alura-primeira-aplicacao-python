


try: 
  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))
  print(num1 / num2)
except ZeroDivisionError:
  print("Não é possível dividir por zero!")


