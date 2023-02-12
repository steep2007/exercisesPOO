# 1- Classe "Pessoa": Crie uma classe chamada "Pessoa" que tenha dois atributos: "nome" e "idade".
# Adicione um método "mostrar_dados" que exibe esses dados.

idade = int(input('Digite sua idade: '))
nome = input('Digite seu nome: ')

class Pessoa():

    def __init__(self, idade, nome):
        self.__idade = idade
        self.__nome = nome

    def mostrarDados(self):
        print(self.__idade)
        print(self.__nome)

objeto = Pessoa(idade, nome)
objeto.mostrarDados()
