from config.mySql import db
from fastapi import HTTPException


cursors = db.cursor(dictionary=True)

# show list of friends
def methodGet(): 
   
    cursors.execute("select * from usuario")
   
    mySql = cursors.fetchall()

   
    return {"user":mySql}

# Filter to account
def methodGetId(item_id:int):    

    cursors.execute("select * from cuenta where id_cuenta = %s",(item_id,))
    
    mys = cursors.fetchone()

    if not mys:
          raise HTTPException(status_code = 404, detail = "account not found")

    
    return {"item_id":item_id,"user":mys}
    

# lista de cosas que tengo que hacer aqui: 
#  Crear el method get para ver a las personas que tengo agregadas (not is import)
#  Crear el method post para agregar alguien y enviar el dinero (import)
#  Crear el method delete para eliminar una persona que no me agrada (not is import)
#  verificar si en verdad existe esa persona (import) 