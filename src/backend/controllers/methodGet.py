from fastapi import (Depends,Request,HTTPException)

from typing import Annotated

from services.authentication import verificationToken

from middleware.roles import roles

from model.Response_models import BaseAccount
def methodGet():    
    return {"user":"hello world"}


def methodGetId(rol_user:str, item_id:int, verify_token:Annotated[str,Depends(verificationToken)]): 
 
    if verify_token["id"] is not item_id:
          raise HTTPException(status_code=403, detail="account not found")
    else: 
        return roles(item_id,rol_user)



#! Lo que esta falatando por hacer en la primera fase:

# Ver la forma de ajustar el problema del time #! import

# Ahora debemos decodificacion al momento de incresar datos del cliente

# Agregar la pestana para ver la lita de pagos que se han hecho durante los dias,semanas y meses del ano 


 
 