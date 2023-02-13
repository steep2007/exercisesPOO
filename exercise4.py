# 4- Classe "Veículo": Crie uma classe chamada "Veículo" que tenha três atributos: "marca", "modelo" e "ano".
# Adicione um método "mostrar_dados" que exibe esses dados.

marca = input('')
modelo = input('')
ano = int(input(''))

class Veiculo():

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrarDados(self):
        print(f' Marca: {self.marca} \n Modelo: {self.modelo} \n Ano: {self.ano}')

objeto = Veiculo(marca, modelo, ano)
objeto.mostrarDados()