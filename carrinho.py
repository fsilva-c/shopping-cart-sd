from Pyro5.api import expose

@expose
class Carrinho(object):
    
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def limpar(self):
        self.itens = []

    def get_itens(self):
        return self.itens