from cliente import Cliente
from item import Item

class Carrinho():

    def __init__(self, cliente: Cliente):
        self.__cliente = cliente
        self.__itens   = []

    def get_itens(self):
        return self.__itens

    def get_cliente(self):
        return self.__cliente

    def limpar(self):
        self.__itens = []
    
    def adicionar(self, item: Item):
        self.__itens.append(item)

    def imprimir_itens(self):
        for item in self.__itens:
            print(f"Produto: {item.get_produto().get_nome()} Preço: {item.get_produto().get_preco()} Quantidade: {item.get_quantidade()}")

