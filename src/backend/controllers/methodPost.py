# Model
from model.Models import (User,Transaction)

# Redirection
from fastapi.responses import RedirectResponse , JSONResponse 

# authentication 
from services.authentication import authentication

from typing import Annotated


from fastapi import Depends

#validate user
from dependencies.filter_data import validateUser



# Poner los manejadore de error como una depends

# validate if the user exists
def methodPost(user:User):  

     result = validateUser(user)
    
     if result is None:
            # responser de header que el login is invalid 
            responder = JSONResponse(status_code=401, content={"content":"invalid user or invalid key"}, headers={"WWW-Authenticate":"Bearer error=invalid_credentials"})
           
            responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")
           
            return responder      
     else:
       
         token = authentication({"id":result[0], "user":result[1]}) #!-----> pass as a dependency
  
         responder =  RedirectResponse(url=f"/banco/saldo/{result[0]}", status_code=301) 
 
         responder.set_cookie(key="session_token", value=token, httponly=True, expires=3600, samesite="lax", path=f"/banco/saldo/{result[0]}" )

         return responder 





# Transaction of money
# def methodPostTransaction(transaction:Transaction):
      
#       #Comparison between password and token 
     
#      sql = ("insert into transaccion" "(tipo_transaccion, fecha_hora , monto , cuenta_id, dispositivo_id)" "values(%s,%s,%s,%s,%s)")
     
#      insert = (transaction.typeTransaction, transaction.date_hour, transaction.moto, transaction.id_account,transaction.id_device ) 
     
#      try:
       
#         cursors.execute(sql,insert)
#         db.commit()     # error here

#      except db.Error as e:
          
#           db.rollback()
         
#          #! This can be handled with a dependency
#          # 401 not authentificaion 
#          # 403 not have permiso
#          # 422 datos de la tranferencia son invalidos 

#          #  add status code 401, 403, 422 
#           responder = JSONResponse(status_code=401, content="invalid user or invalid key", headers={"WWW-Authenticate":"Bearer error=invalid_credentials"})

#           responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")

#      return {"message":"transaction completed successfully"} 


# Lista por hacer en estos prosimos 40 minutos o mas tiempo

# Capturar el token por method get, y validarlo 