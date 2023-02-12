# 2- Classe "Livro": Crie uma classe chamada "Livro" que tenha três atributos: "título", "autor" e "páginas".
# Adicione um método "mostrar_dados" que exibe esses dados.

titulo = input('Digite o titulo do seu livro: ')
autor = input('Digite o autor do seu livro: ')
paginas = input('Digite o total de paginas do seu livro:')

class Livros():

    def __init__(self, titulo, autor, paginas):

        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def mostrarDados(self):
        print(self.__titulo)
        print(self.__autor)
        print(self.__paginas)

objeto = Livros(titulo, autor, paginas)
objeto.mostrarDados()