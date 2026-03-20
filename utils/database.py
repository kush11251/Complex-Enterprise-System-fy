# Import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the engine
engine = create_engine('sqlite:///database.db')

# Create the session
Session = sessionmaker(bind=engine)