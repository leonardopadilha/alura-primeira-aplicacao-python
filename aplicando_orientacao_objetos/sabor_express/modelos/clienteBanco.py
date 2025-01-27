from contaBancaria import ContaBancaria

class ClienteBanco:
  def __init__(self, nome, idade, endereco, cpf, profissao):
    self._nome = nome   
    self.idade = idade
    self.endereco = endereco
    self.cpf = cpf
    self.profissao = profissao

  def __str__(self):
    return f""" 
      Cliente: {self._nome}, 
      Endereço: {self.endereco}, 
      Documento: {self.cpf}, 
      Profissão: {self.profissao} 
    """
  
  @property
  def nome(self):
    return self._nome
  
  @classmethod
  def criar_conta(cls, titular, saldo_inicial):
    conta = ContaBancaria(titular, saldo_inicial)
    return conta

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("João", 40, "Rua C", "111.222.333-44", "Frontend")

print(cliente1)

conta_client1 = ClienteBanco.criar_conta(cliente1.nome, 200)
print(f"Conta de {conta_client1.titular} criada com saldo inicial de R${conta_client1.saldo}")