from config.mySql import db

def methodGet(): 
    cursors = db.cursor()
    cursors.execute("select * from usuario")
    mySql = cursors.fetchall()
    return {"user":mySql}
        
    

