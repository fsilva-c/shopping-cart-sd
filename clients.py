import random
from Pyro5.api import Proxy
import Pyro5

port = 34661
shop = Proxy("PYRO:example.warehouse@localhost:" + str(port))

''' Novo cliente '''
client_name = input("Informe seu nome: ")
client_cart = shop.enter(client_name)

goods = list(shop.goods().keys())

client_cart.purchase(goods[0])
client_cart.purchase(goods[0])
client_cart.purchase(goods[1])
client_cart.purchase(goods[5])

print(f"Seu carrinho: {client_cart.getContents()}")

try:
    input("Confirmar pagamento? ")
    receipt = shop.payByName(client_name)
except Exception:
    print("ERROR: %s" % ("".join(Pyro5.errors.get_pyro_traceback())))

print(f"{client_name} got this receipt:", client_name)
print(receipt)

try:
    shop.leave(client_name)
except Exception:
    print("".join(Pyro5.errors.get_pyro_traceback()))

print(f"{client_name} saiu do mercado")
