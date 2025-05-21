from model.Models import User,Transaction
from config.mySql import db
from fastapi import HTTPException
from fastapi.responses import RedirectResponse

cursors = db.cursor() 

# validate if the user exists

def methodPost(user:User):
      
        sql = ("select id, nombre, password from usuario where nombre = %s and password = %s")
      
        insertData = (user.name,user.password)
      
     # Driver error  
        cursors.execute(sql,insertData)

        mys = cursors.fetchone()
        
        # asking if the user exists
        if not mys:
             raise HTTPException(status_code = 404, detail = "user not finding")

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
