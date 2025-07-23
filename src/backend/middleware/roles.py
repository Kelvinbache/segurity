from config.mySql import db

from fastapi.responses import JSONResponse

from fastapi import HTTPException

from model.Response_models import Account, BaseAccount

cursors = db.cursor(dictionary=True)


def roles(user_id: int, rol_user: str):
    
    match rol_user:      
          case "cliente":
                return get_client(user_id)   

          case "administrador":           
                return get_admin(user_id)

          case _:
              raise HTTPException(status_code=400, detail="you have another role")


def get_client(user_id:int):

    cursors.execute("select * from cuenta where id_cuenta = %s",(user_id,)) 
    mys = cursors.fetchone()
    
    if not mys:
        raise HTTPException(status_code=404, detail="account not found")

    account = Account(**mys).model_dump()

    client_response = BaseAccount(**account).model_dump()
    responder = JSONResponse(content={"item_id": user_id, "user": str(client_response)})

    return responder
         
def get_admin(user_id:int):
    cursors.execute("select * from cuenta where id_cuenta = %s",(user_id,)) 
    mys = cursors.fetchone()
    
    if not mys:
        raise HTTPException(status_code=404, detail="account not found")

    account = Account(**mys).model_dump()
    responder = JSONResponse(content={"item_id": user_id, "user": str(account)})

    return responder