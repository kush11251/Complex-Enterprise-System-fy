# Import FastAPI and controllers
from fastapi import APIRouter
from controllers import user_controller

# Create the router
router = APIRouter()

# Define routes
@router.get("/users")
def get_users():
    return user_controller.get_users()
