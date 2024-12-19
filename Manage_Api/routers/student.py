from fastapi import APIRouter,Depends,HTTPException,status
from ..models import Student_Model
from ..schemas import Student_Schemas,User_Response
from sqlalchemy.orm import Session
from ..database import get_db
from ..outh2 import user_dependency

router=APIRouter(tags=['Student'])



@router.post('/create_student')
def create_student(user:user_dependency,request: Student_Schemas,db:Session=Depends(get_db)):
    get_student=db.query(Student_Model).filter(Student_Model.email==request.email).first()
    if not get_student:
        new_student=Student_Model(email=request.email,full_name=request.full_name,gender=request.gender)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return User_Response(msg='Created Successfully')
    else:
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail='email already exists')
    


@router.get('/get_all_student')   
def get_all_student(user:user_dependency,db:Session=Depends(get_db)):
    user=db.query(Student_Model).all()
    return user

@router.get('/get_student/{sudent_id}')
def get_student(user:user_dependency,student_id:int,db:Session=Depends(get_db)):
    student=db.query(Student_Model).filter(Student_Model.id==student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with {student_id} is not present")
    return student

@router.put('/update_student{id}')
def update_student(id,request:Student_Schemas,db:Session=Depends(get_db)):
    query=db.query(Student_Model).filter(Student_Model.id==id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"student with {id} is not present")
    query.update(request.dict())
    db.commit()
    return 'updated'

@router.delete('/student_delete/{id}')
def destrosdy_student(id,db:Session=Depends(get_db)):
    query=db.query(Student_Model).filter(Student_Model.id==id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"query with {id} is not found")
    db.delete(query)
    db.commit()
    return 'done'



