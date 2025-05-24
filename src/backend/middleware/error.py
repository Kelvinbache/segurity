from fastapi import HTTPException, Request 
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

async def driver(request:Request, call_next):
       
        try:  
          return await call_next(request)

        # exceptions controllers  
        except HTTPException as e:
              return JSONResponse(status_code= e.status_code, content= {"error":e.detail})
              
        # exceptions not controllers
        except Exception as exception:
              return JSONResponse(status_code= 500, content=jsonable_encoder({"error":"error in server", "detail":exception}) )
                  
            
async def validation_exceptions_handler(request, ext):
       return JSONResponse (status_code=400, content= jsonable_encoder({"error":"invalid data", "detail":ext.errors() } ) )                 