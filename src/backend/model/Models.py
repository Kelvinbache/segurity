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


# account of user
# class Account(BaseModel):
#     typeAccount:str
#     numberAccount:str
#     balance:float
#     opening_date:datetime | None


# Pasos de hoy:
# 1) modificar la tabla de usuario y solo poner usuario y contrasena, y validar si existen
# 2) conectar la transaccion con el method post
# 3) validar el saldo para hacer la transferencia
#