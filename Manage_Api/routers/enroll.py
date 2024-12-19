from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..schemas import Enroll_Schemas
from ..database import get_db
from ..models import Enrollment_Model

router=APIRouter(tags=['Enroll'])
get_db=get_db


@router.post('/add_enroll')
def create_enroll(requet:Enroll_Schemas,db:Session=Depends(get_db)):
    enroll=db.query(Enrollment_Model).filter(Enrollment_Model.student_id==requet.student_id and Enrollment_Model.course_id==requet.course_id).first()
    if not enroll:
        create=Enrollment_Model(student_id=requet.student_id,course_id=requet.course_id)
        db.add(create)
        db.commit()
        db.refresh(create)
        return create
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'enroll with id is already exists')

@router.get('/get_all_enroll')
def get_all_enroll(db:Session=Depends(get_db)):
    return db.query(Enrollment_Model).all()


@router.delete('/enroll_delete/{id}')
def destroy_enroll(id : int, db:Session=Depends(get_db)):
    query=db.query(Enrollment_Model).filter(Enrollment_Model.id==id).first()
    if not query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='query with {id} not found')
    db.delete(query)
    db.commit()
    return {'delete done'}