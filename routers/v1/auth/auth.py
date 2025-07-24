from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import Annotated
from internal.auth.auth import AuthenticationCore

class AuthSignInCredentials(BaseModel):
    email: str
    password: str

router = APIRouter(
    tags=["Authentication"]
)

authenticationCore=AuthenticationCore()

@router.post("/signin")
def signin(credentials: Annotated[AuthSignInCredentials, Body(embed=True)]):
    token = authenticationCore.create_token({"email" : credentials.email , "password": credentials.password})
    return {"message": {"token" : token}}