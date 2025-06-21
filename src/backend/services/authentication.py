from authlib.jose import (jwt, JoseError)

from authlib.jose.errors import (InvalidClaimError, DecodeError, BadSignatureError, MissingClaimError, ExpiredTokenError)

from fastapi import (Cookie, HTTPException, Depends)

from typing import Annotated

from datetime import (datetime,timezone,timedelta)

from config.config import config_data

from model.Models import (Payload,Token)


key=config_data["TOKEN"]

header= {'alg':'HS256'}     


def authentication(data:dict) -> Token: 
    
    to_encode=data.copy() 

    exp_token = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp":exp_token})
    
    try:  
     
        jwt_claims = jwt.encode(header, to_encode, key)
        
        jwt_dirty=str(jwt_claims) #?------> pass the token to str  
        
        jwt_clear= jwt_dirty[2:-1] #?-----> clear the token // pass to config clear token 

        return Token(session_token=jwt_clear, type_token="access")
          
    except DecodeError:
           raise HTTPException(status_code=400, detail=f"Invalid authentication token format, problem:")
    
    
    except JoseError as error_token:
           raise HTTPException(status_code=400, detail=f"{error_token}")
          

def verificationToken(session_token:Annotated[str | None, Cookie()]= None):



    if session_token is None: 
         raise HTTPException(status_code=404, detail="cookie not found")

    if  isinstance(session_token, str):
                   
            try: 
                claim = jwt.decode(session_token, key)
                return True

            except BadSignatureError as signature:
                   raise HTTPException(status_code=401, detail=f"invalid signature of token {signature}")

            except (InvalidClaimError,MissingClaimError) as invalid:
                   raise HTTPException(status_code=401, detail=f"the token is invalid {invalid}") #--------> send it to another route
            
            except ExpiredTokenError as exp_token:
                   Refresh_token(session_token)
                   raise HTTPException(status_code=403, detail=f"the token is expire {exp_token}")
    
            except JoseError as error_token:
                   raise HTTPException(status_code=401, detail=f"{error_token}")


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
              raise HTTPException(status_code=400, detail=f"{error_token}")
                    
        
# ! List for complete
# ? 1) refers token
# ? 2) model of tokens with their permits 

# Ideas of complement
# --------------------------------------------------------------------------------------------
# 3) Ask the user to enter their password before making the transfer.
# 4) Refresh the token every 10 minutes
# 6) new model of tokens
# 8) get model session token
# ---------------------------------------------------------------------------------------------


# Manejar los errores al momento de comparar los tokens o cuando no estamos recibiendo nada 

#? implementar una comparacion entre token y clave(especial) de transferencia (password of inicio)

#! Definir en los headers los permisos que tendra el usuario (Importante ver como podemos responder con uno, y pasarle una luego redirecionarlo a su perfil como tal)

# Ver como puedo almacenar un token, y luego compararlo (en 10 minutos)(Caso en la session globlales)

# Enviar la respuesta como un header, y capturarla 

# Agregar dependencias a las rutas para manejar los datos que van llegando

