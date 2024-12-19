from sqlalchemy import Column,String,Integer,Date,TIMESTAMP,ForeignKey
from .database import Base
from datetime import datetime,date
from sqlalchemy.orm import relationship

class Student_Model(Base):
    __tablename__='StudentData'
    id=Column(Integer,primary_key=True,index=True)
    full_name=Column(String(100))
    email=Column(String(255),unique=True)
    gender=Column(String(50))
    created_on=Column(TIMESTAMP,default=datetime.utcnow)

    enrollment=relationship('Enrollment_Model',back_populates='student')

class Course_Model(Base):
      __tablename__='courses'
      id=Column(Integer,primary_key=True,index=True)
      name=Column(String(100),unique=True)

      enrollment=relationship('Enrollment_Model',back_populates='course')

class  Enrollment_Model(Base):
       __tablename__='Enrollment'
       id=Column(Integer,primary_key=True,index=True)
       student_id=Column(Integer,ForeignKey("StudentData.id"))
       course_id=Column(Integer,ForeignKey("courses.id"))
       enrolled_at=Column(TIMESTAMP,default=datetime.utcnow)

       student=relationship('Student_Model',back_populates='enrollment')
       course = relationship("Course_Model", back_populates="enrollment")


class Admin_Model(Base):
      __tablename__='admin'
      id=Column(Integer,primary_key=True,index=True)
      username=Column(String(100),unique=True)
      email=Column(String(255),unique=True)
      password=Column(String(255))
      role=Column(String(100))
      created_on=Column(TIMESTAMP,default=datetime.utcnow)
    


