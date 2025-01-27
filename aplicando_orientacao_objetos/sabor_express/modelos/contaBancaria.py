class ContaBancaria:
  def __init__(self, titular, saldo):
    self._titular = titular.title()
    self._saldo = saldo
    self._ativo = False

  @property
  def titular(self):
    return self._titular
  
  @property
  def saldo(self):
    return self._saldo
  
  @property
  def ativo(self):
    return self._ativo

  def __str__(self):
    return f"Conta de {self._titular} - Saldo: R${self._saldo}"
  
  @classmethod
  def ativar_conta(cls, conta):
    conta._ativo = True
  

conta1 = ContaBancaria("joão", '1000')
conta2 = ContaBancaria("maria", 500)

print(conta1)
print(conta2)

conta3 = ContaBancaria("carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")

conta4 = ContaBancaria("fernando", 1500)
print(f"Titular da conta 4: {conta4.titular}")


