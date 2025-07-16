# import the server
from fastapi import (FastAPI, Request, Response, Cookie)
from fastapi.exceptions import RequestValidationError
from typing import Annotated
import uvicorn

# import the router
from routers.router import router as router_user
from routers.transacciones import router as router_transaction

#Driver error global
from middleware.error import driver,validation_exceptions_handler


app = FastAPI()

# add middleware 
app.middleware("http")(driver)

# add errs specific
app.add_exception_handler(RequestValidationError, validation_exceptions_handler)


# include all the routers
app.include_router(router_user)
app.include_router(router_transaction)


# The port for def
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, server_header=False)


# lista de la cosas que me esta faltando:
# 1) Sacar la informacion del dispositivo y su localizacion
# 2) Agregar la segurida usando encriptadores ( importante saber un poquito mas de cryptografia)
# 5) Hacer como Binace para que te llegue un mesaje al correo sonbre la transferencia o mensajes normales
# 6) investigar como puedo hacer para bloquear una transaccion o la cuenta misma para evitar el robo
# 7) Crer y dejar la creacion de la base de datos y sus tablas

