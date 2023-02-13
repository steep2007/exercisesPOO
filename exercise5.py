# 5- Classe "Conta Bancária": Crie uma classe chamada "ContaBancaria" que tenha três atributos:
# "nome_titular", "numero_conta" e "saldo". Adicione métodos "depositar" e "sacar"
# que permitam fazer depósitos e saques na conta. Adicione um método "mostrar_dados" que exibe esses dados.

nome = input("Nome do titular: ")
numero = int(input("Número da conta: "))
saldo = float(input("Saldo inicial: "))
acao = int(input("Quer sacar (1) ou depositar (0)? "))

class ContaBancaria:
    def __init__(self, nome, numero, saldo):
        self.nomeTitular = nome
        self.numeroConta = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = saldo + valor
        print("Depósito realizado com sucesso!")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = saldo - valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para saque.")

    def mostrar_dados(self):
        print(f"Titular: {self.nomeTitular}")
        print(f"Número da conta: {self.numeroConta}")
        print(f"Saldo: R${self.saldo:.2f}")

conta = ContaBancaria(nome, numero, saldo)

if acao == 0:
    valor = float(input("Quantos você deseja depositar? "))
    conta.depositar(valor)
else:
    valor = float(input("Quantos você deseja sacar? "))
    conta.sacar(valor)

conta.mostrar_dados()
