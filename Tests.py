import unittest

from Product import Product
from product_management import (
    CreateProductCommand,
    GetProductQuery,
    ProductCommandHandler,
    ProductQueryHandler,
)


class TestProductManagement(unittest.TestCase):
    def setUp(self):
        # Initialize handlers for testing
        self.command_handler = ProductCommandHandler()
        self.query_handler = ProductQueryHandler()

    def test_create_product(self):
        # Create a product using the command handler
        command = CreateProductCommand("Product A", 10.99)
        product = self.command_handler.handle_create(command)

        # Verify that the product was created
        self.assertEqual(product.name, "Product A")
        self.assertEqual(product.price, 10.99)

    def test_get_product(self):
        # Create some products for testing
        product1 = Product(1, "Product A", 10.99)
        product2 = Product(2, "Product B", 15.99)
        self.command_handler.products.extend([product1, product2])

        # Retrieve a product using the query handler
        query = GetProductQuery(2)
        retrieved_product = self.query_handler.handle_get(query)

        # Verify that the correct product was retrieved
        self.assertEqual(retrieved_product.product_id, 2)
        self.assertEqual(retrieved_product.name, "Product B")
        self.assertEqual(retrieved_product.price, 15.99)

    def test_get_nonexistent_product(self):
        # Attempt to retrieve a nonexistent product
        query = GetProductQuery(3)
        retrieved_product = self.query_handler.handle_get(query)

        # Verify that the result is None (product not found)
        self.assertIsNone(retrieved_product)


if __name__ == "__main__":
    unittest.main()
