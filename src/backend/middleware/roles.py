from config.mySql import db

from fastapi.responses import JSONResponse

from fastapi import HTTPException

from model.Response_models import Account, BaseAccount, Transaction

cursors = db.cursor(dictionary=True)


def roles(user_id: int, rol_user: str):
    
    match rol_user:      
          case "cliente":
                return get_client(user_id)   

          case "administrador":           
                return get_admin(user_id)

          case _:
              raise HTTPException(status_code=400, detail="you have another role")


#? Method to get client account details
def get_client(user_id:int):

    cursors.execute("select * from cuenta where id_cuenta = %s",(user_id,)) 
    mys = cursors.fetchone()
    
    if not mys:
        raise HTTPException(status_code=404, detail="account not found")

    account = Account(**mys).model_dump()

    client_response = BaseAccount(**account).model_dump()
    responder = JSONResponse(content={"item_id": user_id, "user": str(client_response)})

    return responder

#? Method to get transaction list for a client, debe ir en otro carpeta y archivo         
def listTransactions(user_id:int):
    cursors.execute(" select monto, fecha_hora, numero_cuenta from transaccion a inner join cuenta b on a.cuenta_id = b.id_cuenta where a.cuenta_id = %s",(user_id,))

    mys = cursors.fetchone()
    
    if not mys:
        raise HTTPException(status_code=404, detail="transactions not found")

    transactions = Transaction(monto=mys["monto"], numero_cuenta=mys["numero_cuenta"], fecha_hora=mys["fecha_hora"]).model_dump()

    return JSONResponse(content={"transactions": str(transactions)})


#? Method to get admin account details
def get_admin(user_id:int):
    cursors.execute("select * from cuenta where id_cuenta = %s",(user_id,)) 
    mys = cursors.fetchone()
    
    if not mys:
        raise HTTPException(status_code=404, detail="account not found")

    account = Account(**mys).model_dump()
    responder = JSONResponse(content={"item_id": user_id, "user": str(account)})

    return responder