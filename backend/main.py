from fastapi import FastAPI
from backend.routes import user_routes
from backend.database import init_db

app = FastAPI(title="Pathfinder AI - Backend")

# Initialize database tables
init_db()

# Include routers
app.include_router(user_routes.router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Welcome to the Pathfinder AI Backend"}
