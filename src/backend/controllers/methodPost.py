# Model
from model.Models import User,Transaction

# db
from config.mySql import db

# Error
from fastapi import HTTPException

# Redirection
from fastapi.responses import RedirectResponse


cursors = db.cursor() 

# validate if the user exists

def methodPost(user:User):    
     #Filter the data   
        sql = ("select id, nombre, password from usuario where nombre = %s and password = %s") # select and have condition
      
        insertData = (user.name,user.password)
      
     # Driver error  
        cursors.execute(sql,insertData)

        mys = cursors.fetchone() # -----> None
        
        if not mys:
            raise HTTPException(status_code=401, detail="invalid user or invalid key")

        else:
          
          #redirect to my account
           return RedirectResponse(url=f"/banco/saldo/{mys[0]}", status_code=301) 



# Transaction of money
def methodPostTransaction(transaction:Transaction):
     
     sql = ("insert into transaccion" "(tipo_transaccion, fecha_hora , monto , cuenta_id, dispositivo_id)" "values(%s,%s,%s,%s,%s)")
     
     insert = (transaction.typeTransaction, transaction.date_hour, transaction.moto, transaction.id_account,transaction.id_device ) 
     
     try:
       
        cursors.execute(sql,insert)
        db.commit()     # error here

     except db.Error as e:
          
          db.rollback()
          raise HTTPException(status_code = 400, detail = {"error":e}) 

     return {"message":"transaction completed successfully"} 
