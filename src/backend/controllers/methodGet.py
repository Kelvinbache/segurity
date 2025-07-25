from fastapi import (Depends,Request,HTTPException)

from typing import Annotated

from services.authentication import verificationToken

from middleware.roles import roles, listTransactions

from model.Response_models import BaseAccount

def methodGet():    
    return {"user":"hello world"}


def methodGetId(rol_user:str, item_id:int, verify_token:Annotated[str,Depends(verificationToken)]): 
 
    if verify_token["sub"] is not item_id:
          raise HTTPException(status_code=403, detail="account not found")
    else: 
        return roles(item_id,rol_user)

def methodGetTransactionList(verify_token:Annotated[str,Depends(verificationToken)]): 
    sub = verify_token["sub"]

    if sub is None:
            raise HTTPException(status_code=403, detail="account not found")
    return listTransactions(sub)


# Ver como podemos solucionar el problema de datetime
