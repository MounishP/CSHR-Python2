class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Inventory:
    def __init__(self):
        self.products = []

    def addProduct(self, product):
        self.products.append(product)

    def displayProducts(self):
        for product in self.products:
            print(f"{product.id} : {product.name}")


product1 = Product(1, "laptop")

inventory = Inventory()
inventory.addProduct(product1)
inventory.addProduct(product1)

inventory.displayProducts()
