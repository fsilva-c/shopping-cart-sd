
import time
from Pyro5.api import expose, behavior, Daemon

from carrinho import Carrinho
from produto import Produto
from cliente import Cliente

@expose
@behavior(instance_mode="single")
class LojaFJ(object):
    def __init__(self):
        self.produtos = [
            Produto("001", "Leite", 8.99),
            Produto("002", "Manteiga", 20.00),
            Produto("003", "Leite", 8.99),
            Produto("004", "Ovo", 7.99),
            Produto("005", "Chocolate", 10.00)
        ]
        self.clientes_na_loja = []

    def enter(self, cliente: Cliente):
        print(f"Cliente {cliente.get_nome()} entrou na loja.")
        carrinho = Carrinho(cliente)
        self.clientes_na_loja.append(cliente)
        # self._pyroDaemon.register(carrinho)  # make cart a pyro object
        return carrinho
    

    def clientes(self):
        return self.clientes_na_loja

    def estoque(self):
        return self.produtos

    def pagar(self, carrinho: Carrinho):
        recibo = []
        recibo.append("Data do recibo: " + time.asctime())
        total = 0.0
        for item in carrinho.get_itens():
            preco = item.get_produto().get_preco()
            total += preco
            recibo.append("%13s  %.2f" % (item.get_produto().get_nome(), preco))
        recibo.append("")
        recibo.append("%13s  %.2f" % ("total:", total))
        carrinho.limpar()
        return "\n".join(recibo)

    def sair(self, carrinho : Carrinho):
        print(f"Cliente {carrinho.get_cliente().get_nome()} saiu da loja.")

        if carrinho.get_itens():
            print(" O carrinho não esta vazio")
            raise Exception("Tentativa de roubo")
        self.clientes_na_loja.remove(carrinho.get_cliente())
        self._pyroDaemon.unregister(carrinho)

    def get_produtos(self):
        return self.produtos

# main program
def main():
    Daemon.serveSimple({
        LojaFJ: "trabalhosd.lojaFJ"
    }, ns = False)

if __name__=="__main__":
    main()
