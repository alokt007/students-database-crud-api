from app.database import Base, engine
from app.routes.base import api_router
from fastapi import FastAPI

# Automatically create database tables on startup if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the aggregated router
app.include_router(api_router)

 
@app.get("/", tags=["Root"])
def root():
  return {
      "message": "Welcome to Student Management API. Visit /docs for Swagger UI."
  }