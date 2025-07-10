# Model
from model.Models import (User,Transaction)

# Redirection
from fastapi.responses import RedirectResponse , JSONResponse 

# authentication 
from services.authentication import authentication

from typing import Annotated

from fastapi import (Depends,Request)

#validate user
from dependencies.filter_data import (validateUser, method_transaction, sql_get_amount_currents)


# validate if the user exists
def methodPost(user:User, request:Request):  


     result = validateUser(user)
    
     if result is None:
            # responser de header que el login is invalid 
            responder = JSONResponse(status_code=401, content={"content":"invalid user or invalid key"}, headers={"WWW-Authenticate":"Bearer error=invalid_credentials"})
           
            responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")
           
            return responder      
     else:
       
         token = authentication({"id":result[3], "user":result[1]})
         
         generate_url = request.url_for("home",item_id=result[3]) #---> el posible problema esta en que estoy pasando toda ruta
         
         part_segment=str(generate_url).split("/")
                  
         new_url= "/" + part_segment[3] + "/" + part_segment[4] + "/" + part_segment[5] + "/" + part_segment[6]

         responder =  RedirectResponse(url=new_url, status_code=301) 
 
         responder.set_cookie(key="session_token", value=token.session_token, httponly=True, expires=3600, samesite="lax", path=new_url)

         return responder 




# validate the type of permit
# You should see the contact list with the data (name, ID, phone number, bank)------> #? add db 
# then make a function that simply passes the data and puts the id below without showing much information
# subtract from the account and update account of client  

#ahora aqui vamos a cambiar un quito la forma de entrada, como agregando que la fecha se ponga sola 

# Transaction of money
def methodPostTransaction(transaction:Transaction, check_balance:Annotated[str, Depends(sql_get_amount_currents)]):
      
      result = method_transaction(transaction, check_balance)
     
      return {"message":result} 



