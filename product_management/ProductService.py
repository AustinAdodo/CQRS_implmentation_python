from product_management.CreateProductCommand import CreateProductCommand
from product_management.GetProductQuery import GetProductQuery


class ProductService:
    def __init__(self, command_bus, query_bus):
        self.command_bus = command_bus
        self.query_bus = query_bus

    def create_product(self, name, price):
        command = CreateProductCommand(name, price)
        self.command_bus.handle(command)

    def get_product(self, product_id):
        query = GetProductQuery(product_id)
        return self.query_bus.handle(query)
