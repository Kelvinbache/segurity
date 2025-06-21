from pydantic import BaseModel
from datetime import datetime

# The model person 



# modification of model
class User(BaseModel):
    name:str
    password:str

# Transaction
class Transaction(BaseModel):
    typeTransaction:str
    date_hour:datetime | None
    moto:float
    id_account:int
    id_device:int  

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
    exp:datetime | None

class Token(BaseModel):
    session_token:str
    type_token:str        



# Pasos de hoy:
# 1) validar el saldo para hacer la transferencia
# 2) Validar los datos de entrada