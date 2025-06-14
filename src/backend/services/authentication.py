# libre
from authlib.jose import jwt

from fastapi import (Cookie, HTTPException, Depends)

from typing import Annotated

from datetime import (datetime,timezone,timedelta)

from model.Models import Token


key="The monkey flow"

header= {'alg':'HS256'}     



# from fastapi.security import OAuth2PasswordBearer 


#Header 
# Pass middleware ---> time is make fast ? 
# Pass function for all methods http ---> time is make slow


def authentication(user:dict): 

    to_encode = user.copy()

    exp = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":exp})
    
    # password   
    token = jwt.encode(header, to_encode, key) #converted into a token
    Token(session_token=token, token_type="bearer")   

    return  token



def verificationToken(session_token:Annotated[str | None, Cookie()]= None): 
    s= key.encode('utf-8')

    if session_token is None: 
         raise HTTPException(status_code=404, detail="cookie not found")
    
    try: 
         claim = jwt.decode(session_token, s) #!----> Here this error 
         return True  
    except:
         raise HTTPException(status_code=401, detail="Token invalid")

# List for complete
# --------------------------------------------------------------------------------------------
# 1) get the cookie, for give permissions to the user #!(import) (uses a model to pass and take the token, uses the same as user to receive the key) -----> How to make a valid token model?
# 2) If we have an error with the token, handle it. #!(import)
# 3) Ask the user to enter their password before making the transfer.
# 4) Refresh the token every 10 minutes
# 5) Delete cookies every 10 minutes
# 6) new model of tokens
# 7) create the .env for send keys_secret
# 8) get model session token
# ---------------------------------------------------------------------------------------------


# Manejar los errores al momento de comparar los tokens o cuando no estamos recibiendo nada 

# Investigar como se puede hacer para refrescar un token (en 10 minutos)

#? implementar una comparacion entre token y clave de transferencia (password of inicio)

#! Definir en los headers los permisos que tendra el usuario (Importante ver como podemos responder con uno, y pasarle una luego redirecionarlo a su perfil como tal)

# Ver como puedo almacenar un token, y luego compararlo (en 10 minutos)(Caso en la session globlales)

# Enviar la respuesta como un header, y capturarla 

# Agregar dependencias a las rutas para manejar los datos que van llegando

# Configurar un poquito la base de datos y los modelos, para colocarle los tokens
