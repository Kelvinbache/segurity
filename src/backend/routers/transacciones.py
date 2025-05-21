from fastapi import APIRouter

# Controllers 
from controllers.methodPost import methodPostTransaction

router = APIRouter()

# routers of transactions 

router.post("/transaction")(methodPostTransaction)



