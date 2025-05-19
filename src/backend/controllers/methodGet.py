from config.mySql import db

cursors = db.cursor(dictionary=True)


def methodGet(): 
   
    cursors.execute("select * from usuario")
   
    mySql = cursors.fetchall()

   
    return {"user":mySql}
        
    
def methodGetId(item_id:int):    

    cursors.execute("select * from usuario where id = %s",(item_id,))
    
    mySql = cursors.fetchall()

    print(mySql)

    
    return {"item_id":item_id,"user":mySql}
    
