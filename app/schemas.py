from pydantic import BaseModel,EmailStr
from datetime import datetime




class PostBase(BaseModel):
    title :str
    content :str 
    published : bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id : int
    
    
    # convert to python dictionary
    class Config:
        orm_mode = True

#take email and password
class usercreate(BaseModel):
    email : EmailStr
    password : str

# get email and id
class userout(BaseModel):
    id: int
    email : EmailStr
    class Config:
        orm_mode = True

# Get user password
class userpass(BaseModel):
    password : str
    class Config:
        orm_mode = True

# user login
class userlogin(BaseModel):
    email : EmailStr
    password : str