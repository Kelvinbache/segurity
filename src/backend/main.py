# import the server
from fastapi import FastAPI
import uvicorn

# import the router
from routers.router import router as router_user
from routers.transacciones import router as router_transaction

app = FastAPI()


# include all the routers
app.include_router(router_user)
app.include_router(router_transaction)


# The port for def
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)


# lista de la cosas que me esta faltando:
# 1) Sacar la informacion del dispositivo y su localizacion
# 2) Agregar la segurida usando encriptadores ( importante saber un poquito mas de cryptografia)
# 3) Hacer un manejador de errores para abarcar la mayor posibilida del proyecto 
# 4) Comprobar sip el usuario puede hacer una transferencia con su saldo actual
# 5) Hacer como Binace para que te llegue un mesaje al correo sonbre la transferencia o mensajes normales
# 6) investigar como puedo hacer para bloquear una transaccion o la cuenta misma para evitar el robo