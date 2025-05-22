from pydantic import BaseModel
from datetime import datetime

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



# Pasos de hoy:
# 1) validar el saldo para hacer la transferencia
#