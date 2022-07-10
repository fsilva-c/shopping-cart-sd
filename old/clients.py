from Pyro5.api import Proxy, register_dict_to_class, register_class_to_dict, config
import Pyro5

from produto import Produto

config.SERIALIZER = "json"

from cliente import Cliente
from item import Item

port = 63400
shop = Proxy("PYRO:trabalhosd.lojaFJ@localhost:" + str(port))

# register_class_to_dict(Cliente, Cliente.cliente_to_dict)
# register_dict_to_class("Cliente", Cliente.dict_to_cliente)

register_class_to_dict(Produto, Produto.produto_to_dict)
register_dict_to_class("Produto", Produto.dict_to_produto)

''' Novo cliente '''

produtos_loja = shop.get_produtos()
# carrinho_cliente1 = shop.enter(Cliente("003", "Graziele"))
# carrinho_cliente2 = shop.enter(Cliente("004", "João"))

exit()

carrinho_cliente1.adicionar(Item(produtos_loja[0], 5))
carrinho_cliente1.adicionar(Item(produtos_loja[1], 5))
carrinho_cliente2.adicionar(Item(produtos_loja[2], 4))
carrinho_cliente2.adicionar(Item(produtos_loja[3], 5))

print(f"Seu carrinho: {carrinho_cliente1.imprimir()}")
print(f"Seu carrinho: {carrinho_cliente2.imprimir()}")

try:
    input("Confirmar pagamento? ")
    recibo = shop.pagar(carrinho_cliente1)
except Exception:
    print("ERROR: %s" % ("".join(Pyro5.errors.get_pyro_traceback())))

print(f"O recibo do cliente {carrinho_cliente1.get_cliente().get_nome()}")
print(recibo)

try:
    shop.sair(carrinho_cliente1)
except Exception:
    print("".join(Pyro5.errors.get_pyro_traceback()))

print(f"{carrinho_cliente1.get_cliente().get_nome()} saiu do mercado")
