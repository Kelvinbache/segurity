from config.mySql import db

from fastapi import (Depends,Request,HTTPException)

from fastapi.responses import JSONResponse

from typing import Annotated

from services.authentication import verificationToken

from model.Models import Account


cursors = db.cursor(dictionary=True)


def methodGet(): 
   
    cursors.execute("select * from usuario")
   
    mySql = cursors.fetchall()
   
    return {"user":mySql}


def methodGetId(item_id:int, verify_token:Annotated[str,Depends(verificationToken)]): 

    if verify_token["id"] is not item_id:
          raise HTTPException(status_code=403, detail="account not found")

    else:      
          cursors.execute("select * from cuenta where id_cuenta = %s",(item_id,)) 

          mys = cursors.fetchone()
    
          if not mys:
              raise HTTPException(status_code=401, detail="account not found")
    
          response = Account(**mys).model_dump()         

          responder = JSONResponse(content={"item_id":item_id,"user":str(response)})

          return responder



#! Lo que esta falatando por hacer en la primera fase:

# Ver la forma de ajustar el problema del time #! import

# Ahora debemos decodificacion al momento de incresar datos del cliente

# Cambiar la base de datos por la otra 

# Agregar el protocolo de los roles y permisos al cliente

# Agregar la pestana para ver la lita de pagos que se han hecho durante los dias,semanas y meses del ano 


 
 