from pydantic import BaseModel
from datetime import datetime,date

class BaseAccount(BaseModel):
    numero_cuenta: str 
    saldo: float
    fecha_apertura: datetime | None

class Account(BaseAccount):
    id_cuenta:int
    tipo_cuenta:str
    usuario_id:int
    banco_id:int