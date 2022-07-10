from Pyro5.api import Proxy
import Pyro5

porta = 50739
lojaFJ = Proxy("PYRO:trabalhosd.lojaFJ@localhost:" + str(porta))

''' Novo cliente '''
nome_cliente = input("Informe seu nome: ")
carrinho_cliente = lojaFJ.entrar(nome_cliente)

produtos_loja = list(lojaFJ.produtos().keys())

for i, produto in enumerate(produtos_loja):
    print(f"{i} -> {produto} | {lojaFJ.produtos()[produto]}")

print("Digite -1 para parar de adicionar itens no carrinho")
print("Informe um produto: ")

opcao = 1
while 1:
    opcao = int(input())
    if opcao == -1:
        break
    carrinho_cliente.adicionar(produtos_loja[opcao])

print(f"Seu carrinho: {carrinho_cliente.get_itens()}")

try:
    input("Confirmar pagamento? ")
    recibo = lojaFJ.pagar(carrinho_cliente)
except Exception:
    print("ERROR: %s" % ("".join(Pyro5.errors.get_pyro_traceback())))

print(f"Recibo de {nome_cliente}:", nome_cliente)
print(recibo)

try:
    lojaFJ.sair(nome_cliente)
except Exception:
    print("".join(Pyro5.errors.get_pyro_traceback()))

print(f"{nome_cliente} saiu do mercado")