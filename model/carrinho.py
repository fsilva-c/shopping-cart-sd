from Pyro5.api import expose

from cliente import Cliente
from item import Item

@expose
class Carrinho():

    def __init__(self, cliente: Cliente, itens: Item):
        self.__cliente = cliente
        self.__itens   = itens
