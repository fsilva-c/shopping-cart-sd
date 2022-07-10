import time

from Pyro5.api import expose, behavior, Daemon
from shoppingcart import ShoppingCart

@expose
@behavior(instance_mode="single")
class Shop(object):
    inventory = {
        "pepel": 1.25,
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

    customersInStore = {}

    def enter(self, name):
        print("Customer %s enters the store." % name)
        print("Customer takes a shopping cart.")
        # create a cart and return it as a pyro object to the client
        cart = ShoppingCart()
        self.customersInStore[name] = cart
        self._pyroDaemon.register(cart)  # make cart a pyro object
        return cart

    def customers(self):
        return list(self.customersInStore.keys())

    def goods(self):
        return self.inventory

    def payByName(self, name):
        print("Customer %s goes to the counter to pay." % name)
        cart = self.customersInStore[name]
        return self.payCart(cart, name)

    def payCart(self, cart, name=None):
        receipt = []
        if name:
            receipt.append("Receipt for %s." % name)
        receipt.append("Receipt Date: " + time.asctime())
        total = 0.0
        for item in cart.getContents():
            price = self.inventory[item]
            total += price
            receipt.append("%13s  %.2f" % (item, price))
        receipt.append("")
        receipt.append("%13s  %.2f" % ("total:", total))
        cart.empty()
        return "\n".join(receipt)

    def leave(self, name):
        print("Customer %s leaves." % name)
        cart = self.customersInStore[name]
        print("  their shopping cart contains: %s" % cart.getContents())
        if cart.getContents():
            print("  it is not empty, they are trying to shoplift!")
            raise Exception("attempt to steal a full cart prevented")
        # delete the cart and unregister it with pyro
        del self.customersInStore[name]
        self._pyroDaemon.unregister(cart)


# main program
def main():
    Daemon.serveSimple({
        Shop: "example.warehouse"
    }, ns = False)

if __name__=="__main__":
    main()
