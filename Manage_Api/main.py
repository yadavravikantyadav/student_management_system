from fastapi import FastAPI
from .database import Base,engine
from .routers import student,course,enroll,admin
from .import authentication

app=FastAPI()
Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(admin.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(enroll.router)
    

