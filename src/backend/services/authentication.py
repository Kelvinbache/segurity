from authlib.jose import (jwt, JoseError)

from fastapi import (Cookie, HTTPException)

from typing import Annotated

from datetime import (datetime,timezone,timedelta)

from config.config import config_data

from model.Models import (Payload,Token)

from middleware.error import driver_error

key=config_data["TOKEN"]

header= {'alg':'HS256'}     


def authentication(data:dict) -> Token: 
    
    to_encode=data.copy() 

    exp_token = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp":exp_token})
    
    try:  
     
        jwt_claims = jwt.encode(header, to_encode, key)
        return Token(session_token=jwt_claims, type_token="access")
          
    except JoseError as error_token:
          driver_error(error_token)

def verificationToken(session_token:Annotated[str | None, Cookie()]= None):

    if session_token is None: 
         raise HTTPException(status_code=404, detail="cookie not found")

    if  isinstance(session_token, str):
                   
            try: 
                claim = jwt.decode(session_token, key)
                return claim

            except JoseError as errors:
                   driver_error(errors)
                 
                   

# ----> pass the model of token
# the dato
# the time of use 
# type of token that use the client 

def Refresh_token(token:str) -> Token:

       time_current = int(datetime.now(timezone.utc).timestamp())
      
       try: 

          payload= jwt.decode(token,key)
          
          if  time_current > payload.get("exp"):
              
              exp_token = datetime.now(timezone.utc) + timedelta(minutes=8)
              
              to_encode = Payload(sub=payload.get("id"),userName=payload.get("user"), exp=exp_token)
              
              fresh_token = jwt.decode(headers,to_encode,key)
              
              return Token(session_token=fresh_token, type_token="refresh")

       except JoseError as error_token:
              driver_error(error_token)      
        


# Ideas of complement
# --------------------------------------------------------------------------------------------
# 3) Ask the user to enter their password before making the transfer.
# 4) Refresh the token every 10 minutes
# 6) new model of tokens
# 8) get model session token
# ---------------------------------------------------------------------------------------------


# Manejar los errores al momento de comparar los tokens o cuando no estamos recibiendo nada 

#! Definir en los headers los permisos que tendra el usuario (Importante ver como podemos responder con uno, y pasarle una luego redirecionarlo a su perfil como tal)

# Enviar la respuesta como un header, y capturarla 

# Agregar dependencias a las rutas para manejar los datos que van llegando

