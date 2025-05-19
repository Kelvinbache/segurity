from model.Models import User
from config.mySql import db
from fastapi import HTTPException

cursors = db.cursor() 

# validate if the user exists

def methodPost(user:User):
      
        sql = ("select nombre, password from usuario where nombre = %s and password = %s")
      
        insertData = (user.name,user.password)
      
        cursors.execute(sql,insertData)

        mys = cursors.fetchone()

        # asking if the user exists

        if not mys:

             raise HTTPException(status_code = 404, detail = "user not finding")

        else:

          return {"message":"welcome to banco", "user":user.name}

# Transaction of money



# luego hacer que me muestre el saldo que tengo en la cuenta  