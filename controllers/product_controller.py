# Import services
from services import product_service

# Define the controller
class ProductController:
    def get_products(self):
        return product_service.get_products()