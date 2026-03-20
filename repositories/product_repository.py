# Import models
from models import product_model

# Define the repository
class ProductRepository:
    def get_products(self):
        return product_model.Product.query.all()