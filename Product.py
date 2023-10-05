from unicodedata import decimal


class Product:
    def __init__(self, product_id: int, name: str, price: decimal):
        self.product_id = product_id
        self.name = name
        self.price = price
