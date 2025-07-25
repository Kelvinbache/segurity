from pydantic import BaseModel
from datetime import datetime,date


# modification of model
class User(BaseModel):
    name:str
    password:str

# Transaction
class Transaction(BaseModel):
    typeTransaction:str
    moto:float
    dni:str
    phone:str
    id_device:int
    back:str  

# Device
class Device(BaseModel):
    typeDevice:str
    brand:str
    model:str 
    id_user:int

# Structure of token and fresh token 
class Payload(BaseModel):
    sub:int 
    userName:str
    exp:int| None

class Token(BaseModel):
    session_token:str
    type_token:str        

class Payload_tow(BaseModel):
    sub:int 
    userName:str
    rol:str
    exp:int | None
