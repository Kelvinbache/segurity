from model.Models import User
from config.mySql import db
from fastapi import HTTPException

cursors = db.cursor() 

# validate if the user exists

def methodPost(user:User):
      
        sql = ("select nombre, password from usuario")
      
        insertData = (user.name,user.password)
      
        cursors.execute(sql,insertData)

        mys = cursors.fetchall()
         
         result = filter(user.name == nombre and user.password == password, mys)
      
         if not result:
              raise HTTPException(
                 status_code=404
                 detail="user not finding"
              )

        return {"message":"welcome to banco", "user":user.name}

