from fastapi import FastAPI
from routers.v1.auth import auth
from middleware.auth_middleware import AuthMiddleware

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to messager"

app.add_middleware(AuthMiddleware)

app.include_router(auth.router , prefix="/v1/auth")