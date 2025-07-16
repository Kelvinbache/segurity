from fastapi import APIRouter

# Controllers 
from controllers.methodPost import methodPostTransaction

router = APIRouter( prefix="/v1", tags=["v1"],)

# routers of transactions 

router.post("/transaction")(methodPostTransaction)



