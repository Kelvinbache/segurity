from config.mySql import db

from fastapi import Depends

from fastapi.responses import JSONResponse

from typing import Annotated

# from model.Models import Token, User

from services.authentication import verificationToken

cursors = db.cursor(dictionary=True)


# show list of friends
def methodGet(): 
   
    cursors.execute("select * from usuario")
   
    mySql = cursors.fetchall()
   
    return {"user":mySql}


def methodGetId(item_id:int, verify_token:Annotated[str,Depends(verificationToken)]):    
   
    cursors.execute("select * from cuenta where id_cuenta = %s",(item_id,))
    mys = cursors.fetchone()
    
    if not mys:
          responder = JSONResponse(status_code=404,content="account not found") 
          responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")
          return responder
    
    if verify_token: 
          responder = JSONResponse(content={"item_id":item_id,"user":mys})      
          return responder

# lista de cosas que tengo que hacer aqui: 
#  Crear el method get para ver a las personas que tengo agregadas (not is import)
#  Crear el method post para agregar alguien y enviar el dinero (import)
#  Crear el method delete para eliminar una persona que no me agrada (not is import)
#  verificar si en verdad existe esa persona (import) 