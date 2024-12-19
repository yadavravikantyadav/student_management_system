from passlib.context import CryptContext

pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hash():
    def bcrypt(password:str):
        return pwd_context.hash(password)
    
    def password_verify(plain_password,Hashed_password):
        return pwd_context.verify(plain_password,Hashed_password)