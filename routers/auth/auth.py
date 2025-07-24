from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["authorization"]
)

@router.post("/signin")
def signin(email : str , password : str):
    return { "message" : "Successfully logined" }