# Exception
from fastapi import (HTTPException, Request) 

# Validate the data
from fastapi.exceptions import RequestValidationError

# responser 
from fastapi.responses import JSONResponse

# 
from fastapi.encoders import jsonable_encoder

from authlib.jose.errors import (InvalidClaimError, DecodeError, BadSignatureError, MissingClaimError, ExpiredTokenError)


async def driver(request:Request, call_next):
       
        try:  
          return await call_next(request)

        # exceptions controllers  
        except HTTPException as e:
              return JSONResponse(status_code= e.status_code, content= {"error":e.detail})
              
      #   except Exception as exception:
      #         return JSONResponse(status_code= 500, content=jsonable_encoder({"error":"error in server", "detail":exception}) )


# Validate the data  
async def validation_exceptions_handler(request, ext):
       return JSONResponse (status_code=400, content= jsonable_encoder({"error":"invalid data", "detail":ext.errors() } ) )                 

# encapsulates all the error in tokens
def driver_error(problem:Exception):
  
        if isinstance(problem,BadSignatureError):
            raise HTTPException(status_code=401, detail=f"invalid signature of token {BadSignatureError}")

        if isinstance(problem,InvalidClaimError):
            raise HTTPException(status_code=401, detail=f"the token is invalid {InvalidClaimError}") #--------> send it to another route
        
        if isinstance(problem,MissingClaimError):
            raise HsTTPException(status_code=401, detail=f"the token is invalid {MissingClaimError}") #--------> send it to another route

        if isinstance(problem,ExpiredTokenError):
            raise HTTPException(status_code=403, detail=f"the token is expire {ExpiredTokenError}")
    
        if isinstance(problem,DecodeError):
           raise HTTPException(status_code=400, detail=f"Invalid authentication token format, problem:")

        if isinstance(problem,JoseError):
            raise HTTPException(status_code=401, detail=f"{JoseError}") 
         



# Password invalid 
# async def invalid_credentials(request, call_next):
#         if not data:
#             # responser de header que el login is invalid 
#             responder=HTTPException(status_code=401, detail="invalid user or invalid key", headers={"WWW-Authenticate":"Bearer error=invalid_credentials"})
#             # responder.set_cookie(key="login_error", value="data invalid", httponly=True, expires=3600, samesite="lax")
#             raise responder      
        

  
# Manejar los errores que son de tipo 400 o mas arriba 
# luego pasarlo como middleware antes de ejucutar las rutas como tal 