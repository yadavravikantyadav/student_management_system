from fastapi import APIRouter,Depends,HTTPException,status
from ..database import get_db
from sqlalchemy.orm import Session
from ..models import Admin_Model
from ..schemas import Admin_Schemas
from ..hashing import Hash
from ..outh2 import user_dependency,role_required


router=APIRouter(tags=['Admin'])


@router.post('/create_admin')
def Create_admin(user:user_dependency,request:Admin_Schemas,db:Session=Depends(get_db),role:Admin_Model=Depends(role_required('SuperAdmin'))):
    get_admin=db.query(Admin_Model).filter(Admin_Model.email==request.email).first()
    if not get_admin:
        new_admin=Admin_Model(email=request.email,password=Hash.bcrypt(request.passsword),role=request.role,username=request.username)
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
    raise HTTPException(status_code=status.HTTP_302_FOUND,detail='Admin already exists')

@router.get('/get_all_admin')
def Get_all_admin(user:user_dependency,db:Session=Depends(get_db)):
    get=db.query(Admin_Model).all()
    return get






