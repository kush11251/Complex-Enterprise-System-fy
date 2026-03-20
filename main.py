# Import FastAPI
from fastapi import FastAPI
from routers import user_router, product_router

# Create the app
app = FastAPI()

# Include routers
app.include_router(user_router)
app.include_router(product_router)