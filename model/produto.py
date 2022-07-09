from Pyro5.api import expose

@expose
class Produto():
    
    def __init__(self, codigo, nome, preco):
        self.__codigo = codigo
        self.__nome   = nome
        self.__preco  = preco

    
    # getters and setters...
    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco
