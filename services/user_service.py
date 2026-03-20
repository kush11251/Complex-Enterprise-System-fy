# Import repositories
from repositories import user_repository

# Define the service
class UserService:
    def get_users(self):
        return user_repository.get_users()