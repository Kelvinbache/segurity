from fastapi import HTTPException, Request 
from fastapi.responses import JSONResponse

async def driver(request:Request, call_next):
       
        try:
        
          return await call_next(request)
       
        # exceptions controllers  
        except HTTPException as e:
              return JSONResponse(status_code=e.status_code, content= {"error":e.detail})
       
        # exceptions not controllers
        except Exception as exception:
              return JSONResponse(status_code= 500, content= {"error":"error in server", "detail":str(exception)})
                  
            
                