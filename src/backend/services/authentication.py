from authlib.jose import (jwt, JoseError)

from fastapi import (Cookie, HTTPException)

from typing import Annotated

from datetime import (datetime,timezone,timedelta)

from config.config import config_data

from model.Models import (Payload,Token, Payload_tow)

from middleware.error import driver_error

key=config_data["TOKEN"]

header= {'alg':'HS256'}     


def authentication(data:dict) -> Token: 
    
    exp_token = int((datetime.now(timezone.utc) + timedelta(minutes=15)).timestamp())
    payload = Payload_tow(sub=data.get("id"), userName=data.get("user"), rol=data.get("rol"), exp=exp_token)

    try:  
        jwt_claims = jwt.encode(header, payload.model_dump(), key)
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
                 
                   

def Refresh_token(token:str) -> Token:

       time_current = int(datetime.now(timezone.utc).timestamp())
      
       try: 

          payload= jwt.decode(token,key)
          
          if  time_current > payload.get("exp"):
              
              exp_token = datetime.now(timezone.utc) + timedelta(minutes=8)
              
              to_encode = Payload(sub=payload.get("id"),userName=payload.get("user"), exp=exp_token)
              
              fresh_token = jwt.decode(headers,to_encode.model_dump(),key)
              
              return Token(session_token=fresh_token, type_token="refresh")

       except JoseError as error_token:
              driver_error(error_token)      
        


