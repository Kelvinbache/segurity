from config.mySql import db

from fastapi import Depends,Request

from fastapi.responses import JSONResponse

from typing import Annotated

from services.authentication import verificationToken

from model.Models import Account



cursors = db.cursor(dictionary=True)


# show list of friends
def methodGet(): 
   
    cursors.execute("select * from usuario")
   
    mySql = cursors.fetchall()
   
    return {"user":mySql}


def methodGetId(item_id:int,request:Request,verify_token:Annotated[str,Depends(verificationToken)]):    
   
    cursors.execute("select * from cuenta where id_cuenta = %s",(item_id,))
    mys = cursors.fetchone()
    
    response=Account(**mys).model_dump()

    generate_url = request.url_for("pay")
         
    part_segment=str(generate_url).split("/")
                  
    new_url= "/" + part_segment[3] + "/" + part_segment[4]
    

    if not mys:
          responder = JSONResponse(status_code=404,content="account not found") 
          responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")
          return responder
    
    if verify_token: 
          responder = JSONResponse(content={"item_id":item_id,"user":str(response)})
          responder.set_cookie(key="user", value=item_id, httponly=True, expires=3600, samesite="lax", path=new_url)       
          return responder



#! Objectivos para el dia siguiente:
# Ver la forma de ajustar el problema del time
# Ver que detalles se pueden mejorar y quitar 
# Ahora debemos decodificacion al momento de incresar datos del cliente


# lista de cosas que tengo que hacer aqui: 
#  Crear el method get para ver a las personas que tengo agregadas (not is import)
#  Crear el method post para agregar alguien y enviar el dinero (import)
#  Crear el method delete para eliminar una persona que no me agrada (not is import)
#  verificar si en verdad existe esa persona (import) 