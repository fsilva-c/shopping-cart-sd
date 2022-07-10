import time

from Pyro5.api import expose, behavior, Daemon
from carrinho import Carrinho

@expose
@behavior(instance_mode="single")
class LojaFJ(object):

    produtos_loja = {
        "papel": 1.25,
        "pao": 1.50,
        "carne": 5.99,
        "leite": 0.80,
        "maca": 2.65,
        "chocolate": 3.99,
        "pasta": 0.50,
        "sal": 1.20,
        "pepino": 1.40,
        "biscoito": 1.99,
        "pizza": 3.60,
        "shampoo": 2.22,
        "cerveja": 24.99
    }

    clientes_na_loja = {}

    def entrar(self, nome):
        print(f"Cliente {nome} entrou na loja.")

        carrinho = Carrinho()
        self.clientes_na_loja[nome] = carrinho
        self._pyroDaemon.register(carrinho)

        print(f"Clientes na loja: {self.clientes()}")

        return carrinho

    def clientes(self):
        return list(self.clientes_na_loja.keys())

    def produtos(self):
        return self.produtos_loja

    def pagar(self, carrinho):
        recibo = []
        recibo.append("Data: " + time.asctime())

        total = 0.0
        for item in carrinho.get_itens():
            preco = self.produtos_loja[item]
            total += preco
            recibo.append("%13s  %.2f" % (item, preco))

        recibo.append("")
        recibo.append("%13s  %.2f" % ("total:", total))

        carrinho.limpar()

        return "\n".join(recibo)

    def sair(self, nome):
        carrinho = self.clientes_na_loja[nome]
        print(f"Cliente {nome} saiu da loja.")

        if carrinho.get_itens():
            print(" O carrinho não esta vazio")
            raise Exception("Tentativa de roubo")

        del self.clientes_na_loja[nome]
        self._pyroDaemon.unregister(carrinho)

        print(f"Clientes na loja: {self.clientes()}")

# main program
def main():
    Daemon.serveSimple({
        LojaFJ: "trabalhosd.lojaFJ"
    }, ns = False)

if __name__=="__main__":
    main()