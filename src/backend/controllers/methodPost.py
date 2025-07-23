# Model
from model.Models import (User,Transaction)

# Redirection
from fastapi.responses import RedirectResponse , JSONResponse 

# authentication 
from services.authentication import authentication,verificationToken

from typing import Annotated

from fastapi import (Depends,Request, HTTPException)

#validate user
from dependencies.filter_data import (validateUser, method_transaction, sql_get_amount_currents)


# validate if the user exists
def methodPost(user:User, request:Request):  

     result = validateUser(user)
    
     if result is None:
              raise HTTPException(status_code=401, detail="account not found", headers={"WWW-Authenticate":"Bearer error=invalid_credentials"})           
     else:
         
         token = authentication({"id":result[0], "user":result[1], "rol":result[3]})
         
         generate_url = request.url_for("home",rol_user=result[3],item_id=result[0]) #----> puede ser vas reducido, pasando un directorio 
         
         part_segment=str(generate_url).split("/")
                  
         new_url= "/" + part_segment[3] + "/" + part_segment[4] + "/" + part_segment[5] + "/" + part_segment[6] + "/" + part_segment[7]

         responder =  RedirectResponse(url=new_url, status_code=301) 
 
         responder.set_cookie(key="session_token", value=token.session_token, httponly=True, expires=3600, samesite="lax", path="/")  

         return responder 



# Transaction of money
def methodPostTransaction(transaction:Transaction, verify_token:Annotated[str,Depends(verificationToken)]):
      
      check_balance = sql_get_amount_currents(verify_token["id"])
      
      result = method_transaction(transaction, check_balance)
     
      return {"message":result} 

