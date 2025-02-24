from abc import ABC, abstractmethod

class Veiculo(ABC):
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self._ligado = False

  def __str__(self):
    status = "Ligado" if self._ligado else "desligado"
    return f"{self.marca} {self.modelo} - Status {status}" 
  
  def ligar(self):
    pass