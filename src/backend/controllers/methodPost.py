# Model
from model.Models import User,Transaction

# db
from config.mySql import db

# Redirection
from fastapi.responses import RedirectResponse , JSONResponse 

# authentication 
from services.authentication import authentication

cursors = db.cursor() 

# Poner los manejadore de error como una depends

# validate if the user exists
def methodPost(user:User):    
     #Filter the data   
        
        sql = ("select id, nombre, password from usuario where nombre = %s and password = %s") # select and have condition
      
        insertData = (user.name,user.password)
   
        # Driver error  
        cursors.execute(sql,insertData)

        mys = cursors.fetchone() # -----> None

        if not mys:

            # responser de header que el login is invalid 
            responder = JSONResponse(status_code=401, content={"content":"invalid user or invalid key"}, headers={"WWW-Authenticate":"Bearer error=invalid_credentials"})
           
            responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")
           
            return responder      

        else:

           token = authentication(mys)

           responder =  RedirectResponse(url=f"/banco/saldo/{mys[0]}", status_code=301) 
         
           #Submit a cookie   
           responder.set_cookie(key="session_token", value=token, httponly=True, expires=3600, samesite="lax", path=f"/banco/saldo/{mys[0]}" )
      
           #redirect to my account
           return  responder



# Transaction of money
def methodPostTransaction(transaction:Transaction):
      
      #Comparison between password and token 
     
     sql = ("insert into transaccion" "(tipo_transaccion, fecha_hora , monto , cuenta_id, dispositivo_id)" "values(%s,%s,%s,%s,%s)")
     
     insert = (transaction.typeTransaction, transaction.date_hour, transaction.moto, transaction.id_account,transaction.id_device ) 
     
     try:
       
        cursors.execute(sql,insert)
        db.commit()     # error here

     except db.Error as e:
          
          db.rollback()
         
         # 401 not authentificaion 
         # 403 not have permiso
         # 422 datos de la tranferencia son invalidos 

         #  add status code 401, 403, 422 
          responder = JSONResponse(status_code=401, content="invalid user or invalid key", headers={"WWW-Authenticate":"Bearer error=invalid_credentials"})

          responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")

     return {"message":"transaction completed successfully"} 


# Lista por hacer en estos prosimos 40 minutos o mas tiempo

# Capturar el token por method get, y validarlo 