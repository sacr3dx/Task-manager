from pydantic import BaseModel, Field

class UserSignIn(BaseModel):
    username: str = Field(..., min_length=1, max_length=30, description='Name of the user')
    password: str

class RegisterUser(BaseModel):
    username: str
    password: str
    email: str

class UserSignOut(BaseModel):
    username: str
