from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        self.__modelo = modelo
        self.__cor = cor
        if preco > 0 :
            self.__preco = preco
        else:
            self.__preco = 0
        self.__tempoDeBateria = tempoDeBateria
    
    @property
    def modelo(self):
        return self.__modelo

    @property
    def cor(self):
        return self.__cor

    @property
    def preco(self):
        return self.__preco

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @preco.setter
    def preco(self, preco):
        if preco >= 0 :
            self.__preco = preco
        else:
            print( "Valor não permitido" )

    @tempoDeBateria.setter
    def tempoDeBateria(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria

    def getinformacoes(self):
        return print(f'Modelo: {self.__modelo}\nCor: {self.__cor}\nPreço: {self.__preco}\nTempo de bateria: {self.__tempoDeBateria} horas')
    
    def cadastrar(self):
        print("Notebook Cadastrado")