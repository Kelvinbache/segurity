from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException, Request 


async def validate(user):
    try: 
      user
    except ValidationError as e:
       return JSONResponse(status_code= 400, content= {"error":e.errors()})
                  