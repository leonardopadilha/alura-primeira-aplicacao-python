


try: 
  num_1 = float(input("Digite o primeiro número: "))
  num_2 = float(input("Digite o segundo número: "))
  print(num_1 / num_2)
except ZeroDivisionError:
  print("Não é possível dividir por zero!")
except Exception as e:
  print(type(e), f" - Ocorreu um erro: {e}")


