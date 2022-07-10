from produto import Produto

class Item():
    
    def __init__(self, produto: Produto, quantidade):
        self.__produto    = produto
        self.__quantidade = quantidade

    
    def sub_total(self):
        return self.__produto.get_preco() * self.__quantidade

    # getters and setters...
    def get_produto(self):
        return self.__produto

    def get_quantidade(self):
        return self.__quantidade