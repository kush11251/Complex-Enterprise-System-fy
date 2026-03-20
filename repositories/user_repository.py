# Import models
from models import user_model

# Define the repository
class UserRepository:
    def get_users(self):
        return user_model.User.query.all()