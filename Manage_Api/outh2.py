from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from .Token import verify_token
from typing import Annotated
from sqlalchemy.orm import Session
from .models import Admin_Model

outh2_scheme=OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token:str=Depends(outh2_scheme)):
    credentials=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Could not validate credential')
    return verify_token(token,credentials)


def role_required(required_role: str): 
    def role_checker(current_user: Admin_Model = Depends(get_current_user)): 
        if current_user.role != required_role: 
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions") 
        return current_user 
    return role_checker

user_dependency=Annotated[Session,Depends(get_current_user)]