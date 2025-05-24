from model.Models import User
from config.mySql import db
             
# Here parameters 
def methodPatch(item_id:int,user:User): 
 
    sql = ("update usuario set nombre = %s, apellido = %s, email = %s, telefono = %s where id = %s")
 
    data = (user.name,user.password)
 
    db.cursor().execute(sql,data)
 
    db.commit()
 
    return {"item_id":item_id, "message":"updata with exit", "body":person}


# Idea para este apartado:
# Actualizar la contrasena (enviar un codigo al movil, o autentificador de google)
# Actualizar los datos de un contacto  
# Actualizar los datos personales