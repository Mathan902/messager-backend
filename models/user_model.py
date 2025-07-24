from pydrantic import BaseModel

class UserModel(BaseModel):
    name : str
    email : str
    password : str
    role : str = "user"