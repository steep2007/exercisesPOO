# 3- Classe "Aluno": Crie uma classe chamada "Aluno" que tenha três atributos: "nome", "matricula" e "nota".
# Adicione um método "mostrar_dados" que exibe esses dados.

nome = input('Digite o nome do aluno: ')
matricula = int(input('Digite a matricula do aluno: '))
nota = input('Digite a nota do aluno: ')

class Aluno():

    def __init__(self, nome, matricula, nota):
        self.__nome = nome
        self.__matricula = matricula
        self.__nota = nota

    def mostrarDados(self):
        print(f'O nome do aluno é: {self.__nome}')
        print(f'A matricula do aluno é: {self.__matricula}')
        print(f'A nota do aluno é: {self.__nota}')

objeto = Aluno(nome, matricula, nota)
objeto.mostrarDados()
