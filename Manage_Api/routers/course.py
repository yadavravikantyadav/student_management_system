from fastapi import APIRouter,Depends,HTTPException,status
from ..models import Course_Model
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import Course_Schemas
from ..outh2 import user_dependency

router=APIRouter(tags=['Course'])

@router.post('/add_course')
def create_course(user:user_dependency,request:Course_Schemas,db:Session=Depends(get_db)):
    get_course=db.query(Course_Model).filter(Course_Model.name==request.name).first()
    if not get_course:
        query=Course_Model(name=request.name)
        db.add(query)
        db.commit()
        db.refresh(query)
        return query
    raise HTTPException(status_code=status.HTTP_302_FOUND,detail='subject already exists')

@router.get('/get_all')
def get_all_course(user:user_dependency,db:Session=Depends(get_db)):
    all=db.query(Course_Model).all()
    return all

@router.put('/update/{id}')
def update_course(id,request:Course_Schemas,db:Session=Depends(get_db)):
    query=db.query(Course_Model).filter(Course_Model.id==id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"query with {id} is not present")
    query.update(request.dict())
    db.commit()
    return 'updated'

@router.delete('/course_delete/{id}')
def destroy_course(id,db:Session=Depends(get_db)):
    query=db.query(Course_Model).filter(Course_Model.id==id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"query with {id} is not found")
    db.delete(query)
    db.commit()
    return 'deleted done'