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



#! Lo que esta falatando por hacer en la primera fase:
# Ver la forma de ajustar el problema del time
# Ahora debemos decodificacion al momento de incresar datos del cliente
# Cambiar la base de datos por la otra 
# Agregar el protocolo de los roles y permisos al cliente
# Agregar la pestana para ver la lita de pagos que se han hecho durante los dias,semanas y meses del ano 
# Ajustar el protocolo de las cookiens para que viajen ya cuando estamos ingresando a la cuenta, y se ejecuten los demas protocolos de seguridad
# Hacer un test donde recise lo bugs que esta teniendo la aplicacion (uno de los problema esta cuando estamos enviando la cookien)