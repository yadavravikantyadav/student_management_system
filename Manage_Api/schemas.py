from pydantic import BaseModel

class Student_Schemas(BaseModel):
    email:str
    full_name:str
    gender:str

class User_Response(BaseModel):
    msg:str   

class Course_Schemas(BaseModel):
    name:str     

class Enroll_Schemas(BaseModel):
    student_id:int
    course_id:int

class Admin_Schemas(BaseModel):
    email:str
    passsword:str
    role:str    
    username:str

class TokenData(BaseModel):
    username:str | None =None
    role:str