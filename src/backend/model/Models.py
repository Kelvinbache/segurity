from pydantic import BaseModel
from datetime import datetime
# from fastapi.responses import JSONResponse


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
# 2) Validar los datos de entrada