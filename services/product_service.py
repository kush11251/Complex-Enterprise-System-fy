# Import repositories
from repositories import product_repository

# Define the service
class ProductService:
    def get_products(self):
        return product_repository.get_products()