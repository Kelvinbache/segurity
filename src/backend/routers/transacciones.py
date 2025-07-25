from fastapi import APIRouter

# Controllers 
from controllers.methodPost import methodPostTransaction

from controllers.methodGet import methodGetTransactionList

router = APIRouter( prefix="/v1", tags=["v1"],)

# routers of transactions 

router.post("/transaction")(methodPostTransaction)

router.get("/transaction/list")(methodGetTransactionList)



