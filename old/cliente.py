class Cliente(object):

    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome   = nome

    
    # getters and setters...
    def get_cpf(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    @staticmethod
    def dict_to_cliente(classname, data):
        assert classname == "Cliente"
        return Cliente(data["cpf"], data["nome"])

    @staticmethod
    def cliente_to_dict(cliente):
        return {
            "__class__": "Cliente",
            "cpf":  cliente.get_cpf(),
            "nome": cliente.get_nome(),
        }
