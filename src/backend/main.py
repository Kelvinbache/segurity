# import the server
from fastapi import FastAPI
import uvicorn

# import the router
from routers.router import router as myRouter

app = FastAPI()


# include all the routers
app.include_router(myRouter)

# The port for def
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
