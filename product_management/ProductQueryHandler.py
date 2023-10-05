class ProductQueryHandler:
    def __init__(self):
        self.products = []

    def handle_get(self, query):
        for product in self.products:
            if product.product_id == query.product_id:
                return product
        return None
    # Add handlers for other queries like GetAll, Search, etc.
