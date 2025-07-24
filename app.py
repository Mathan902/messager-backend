from fastapi import FastAPI
from routers.auth import auth

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to messager"

app.include_router(auth.router)