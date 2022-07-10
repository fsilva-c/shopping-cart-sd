class Produto(object):
    
    def __init__(self, codigo: str, nome: str, preco: float):
        self.codigo: str = codigo
        self.nome: str   = nome
        self.preco: float  = preco


    @staticmethod
    def dict_to_produto(classname, data):
        assert classname == "Produto"
        return Produto(data["codigo"], data["nome"], data["preco"])

    @staticmethod
    def produto_to_dict(produto):
        return {
            "__class__": "Produto",
            "codigo": produto.codigo,
            "nome"  : produto.nome,
            "preco" : produto.preco
        }
    
    # getters and setters...
    def get_codigo(self) -> str:
        return self.codigo

    def get_nome(self) -> str:
        return self.nome

    def get_preco(self) -> float:
        return self.preco
