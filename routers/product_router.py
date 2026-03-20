# Import FastAPI and controllers
from fastapi import APIRouter
from controllers import product_controller

# Create the router
router = APIRouter()

# Define routes
@router.get("/products")
def get_products():
    return product_controller.get_products()