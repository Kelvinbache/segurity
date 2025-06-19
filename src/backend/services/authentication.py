from authlib.jose import (jwt, JoseError)

from authlib.jose.errors import (InvalidClaimError)

from fastapi import (Cookie, HTTPException, Depends)

from typing import Annotated

from datetime import (datetime,timezone,timedelta)

from config.config import config_data


key=config_data["TOKEN"]

header= {'alg':'HS256'}     


def authentication(user:dict): 

    to_encode = user.copy()

    exp = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp":exp})
    
    try:  
     
        jwt_claims = jwt.encode(header, to_encode, key)
        
        jwt_dirty=str(jwt_claims) #?------> pass the token to str  
        
        jwt_clear= jwt_dirty[2:-1] #?-----> clear the token 

        return jwt_clear #----> pass the token 
              

    except JoseError as error_token:

           raise HTTPException(status_code=401, detail=f"Token invalid{error_token}")
          

def verificationToken(session_token:Annotated[str | None, Cookie()]= None):
    
    if session_token is None: 
         raise HTTPException(status_code=404, detail="cookie not found")

    if  isinstance(session_token, str):
           
            try: 
                claim = jwt.decode(session_token, key) #!----> the header of token not matches
                return True

            except InvalidClaimError as invalid:
                   raise HTTPException(status_code=401, detail=f"the token {invalid}")
    
            except JoseError as error_token:
                   raise HTTPException(status_code=401, detail=f"{error_token}")
     

# List for complete
# --------------------------------------------------------------------------------------------
# 3) Ask the user to enter their password before making the transfer.
# 4) Refresh the token every 10 minutes
# 5) Delete cookies every 10 minutes
# 6) new model of tokens
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
