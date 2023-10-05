from Product import Product


class ProductCommandHandler:
    def __init__(self):
        self.products = []

    def handle_create(self, command):
        product_id = len(self.products) + 1
        product = Product(product_id, command.name, command.price)
        self.products.append(product)
        return product