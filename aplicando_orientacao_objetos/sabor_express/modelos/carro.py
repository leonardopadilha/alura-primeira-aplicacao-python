from modelos.veiculo import Veiculo

class Carro(Veiculo):
  
  def __init__(self, marca, modelo, portas):
    super().__init__(marca, modelo)
    self._portas = portas

  def __str__(self):
    self._ligado = True
    status = "Ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Status {status}"
  
  def ligar(self):
    print(f"O carro {self.modelo} está ligado")