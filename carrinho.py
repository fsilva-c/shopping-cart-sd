from Pyro5.api import expose

@expose
class Carrinho(object):

    def __init__(self, nome_cliente):
        self.itens = []
        self.nome_cliente = nome_cliente

    def adicionar(self, item):
        self.itens.append(item)

    def limpar(self):
        self.itens = []

    def get_itens(self):
        return self.itens

    def get_nome_cliente(self):
        return self.nome_cliente