from datetime import datetime,timedelta
import jwt
from jwt.exceptions import InvalidTokenError
from .schemas import TokenData



SECRET_KEY = "207767c887db3ca317dd9ab05b27ebc3621658e3aee00158d5903e9429190a9b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def Create_token(data:dict):
    encode=data
    expire=datetime.now()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({'exp':expire})
    encode_jwt=jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt


def verify_token(data:str,credentials_excepttion):
    try:
        payload=jwt.decode(data,SECRET_KEY,algorithms=[ALGORITHM])
        email:str=payload.get('email')
        role:str=payload.get('role')
        if email is None or role is None:
            raise credentials_excepttion
        token_data=TokenData(email=email,role=role)
        return token_data
    except InvalidTokenError:
        raise credentials_excepttion
    




