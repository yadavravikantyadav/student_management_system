from fastapi import APIRouter,HTTPException,status,Depends
from .Token import Create_token
from .database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .models import Admin_Model
from .hashing import Hash 

router=APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(Admin_Model).filter(Admin_Model.email==request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user not present")
    
    if not Hash.password_verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='invalid password')
    
    access_token=Create_token(data={'email':user.email,'role':user.role})
    return {'access_token':access_token,"bearer":"bearer"}