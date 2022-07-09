from Pyro5.api import expose

@expose
class Cliente():

    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome   = nome

    
    # getters and setters...
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome
