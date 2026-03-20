# Import services
from services import user_service

# Define the controller
class UserController:
    def get_users(self):
        return user_service.get_users()