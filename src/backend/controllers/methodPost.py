# Model
from model.Models import (User,Transaction)

# Redirection
from fastapi.responses import RedirectResponse , JSONResponse 

# authentication 
from services.authentication import authentication

from typing import Annotated

from fastapi import (Depends,Request)

#validate user
from dependencies.filter_data import (validateUser, validate_transaction, sql_get_amount_currents)

#import 



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
  
         responder =  RedirectResponse(url=f"/v1/banco/saldo/{result[0]}", status_code=301) 
 
         responder.set_cookie(key="session_token", value=token.session_token, httponly=True, expires=3600, samesite="lax", path=f"/v1/banco/saldo/{result[0]}" )

         return responder 




# validate the type of permit
# You should see the contact list with the data (name, ID, phone number, bank)------> #? add db 
# then make a function that simply passes the data and puts the id below without showing much information
# subtract from the account and update account of client  
       
# Transaction of money
def methodPostTransaction(transaction:Transaction, request:Request):
     
      result = validate_transaction(transaction)
     
      new_online = request.url_for("login") #------> Ahora debemos cambiar algunas cosas sobre como estamos enviando las url y recibiendo sus valores
      # new_online_two = request.url_for("home", item_id=1) #---> El problema debe pasar por el proceso de verificacion antes de pasar por aqui

      # id_user = sql_get_amount_currents(new_online)

      # verify sip the account has enough money
      # update the status of the two account  
    
      # selecting the account we are going to transfer
     
      return {"message":new_online} #?------> What is your type of response?


#? Como puedo solucionar el problema de las dependencias ? ----> El problema esta como podemos enviar la ruta

