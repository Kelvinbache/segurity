from config.mySql import db

# method global
cursors = db.cursor()

def methodDelete(item_id:int):
    
    cursors.execute("delete from usuario where id = %s ", (item_id,))
    
    db.commit()  # This applies the changes
    
    return{"item_id":item_id, "message":"delete exit"}