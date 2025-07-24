import os
from dotenv import load_dotenv
from jose import jwt
from datetime import datetime, timedelta

load_dotenv()

AUTH_SECERT_KEY = os.getenv("AUTH_SECERT_KEY")
AUTH_ALGORITHM = "HS256"

class AuthenticationCore:
    def create_token(self , data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, AUTH_SECERT_KEY, algorithm=AUTH_ALGORITHM)

    def verify_token(self , token: str):
        try:
            payload = jwt.decode(token, AUTH_SECERT_KEY, algorithms=[AUTH_ALGORITHM])
            return payload
        except Exception:
            return None