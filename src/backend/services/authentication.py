# libre
from authlib.jose import jwt

# import time
from model.Models import Payload


# Pass middleware ---> time is make fast ? 
# Pass function for all methods http ---> time is make slow



def authentication(user):
   
    header= {'alg':'HS256'} #Header 
    
    # id and name 
    # payload={'id':user[0], 'user':user[1]} #Body
    
    createToken=Payload(**{"sub":user[0], "userName":user[1]})
    claim = payload.get

    # password
    key_private=user[2] #password
    
    token = jwt.encode(header,createToken, key_private) #converted into a token
    return token


# function for verification
# luego pasar el token que recibimos mediante el post
def verificationToken(token):
       
    try:  
         #compares the password with the token (boolean)
        claims = jwt.decode(tokens.token)  #!---------> return error      
         
        if not claims:
           print("token invalid")
        else:
           print(claims)    
   
    except:
           print("Then error for through")    
      

# List for complete
# --------------------------------------------------------------------------------------------
# 1) get the cookie, for give permissions to the user #!(import) (uses a model to pass and take the token, uses the same as user to receive the key) -----> How to make a valid token model?
# 2) If we have an error with the token, handle it. #!(import)
# 3) Ask the user to enter their password before making the transfer.
# 4) Refresh the token every 10 minutes
# 5) Delete cookies every 10 minutes
# 6) Add depends the controllers 
# ---------------------------------------------------------------------------------------------


# Manejar los errores al momento de comparar los tokens o cuando no estamos recibiendo nada 

# Investigar como se puede hacer para refrescar un token (en 10 minutos)

#? implementar una comparacion entre token y clave de transferencia (password of inicio)

#! Definir en los headers los permisos que tendra el usuario (Importante ver como podemos responder con uno, y pasarle una luego redirecionarlo a su perfil como tal)

# Ver como puedo almacenar un token, y luego compararlo (en 10 minutos)(Caso en la session globlales)

# Enviar la respuesta como un header, y capturarla 

# Agregar dependencias a las rutas para manejar los datos que van llegando

