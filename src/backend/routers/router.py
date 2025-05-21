from fastapi import APIRouter

# controllers 
from controllers.methodGet import methodGet,methodGetId
from controllers.methodPost import methodPost
from controllers.methodPut import methodPut
from controllers.methodDelete import methodDelete

# Use multiple routers
router = APIRouter()


# show balance
router.get("/banco")(methodGet)

router.get("/banco/saldo/{item_id}")(methodGetId)

# check if the client exists
router.post("/banco")(methodPost)

router.put("/banco/client/{item_id}")(methodPut)

router.delete("/banco/client/{item_id}")(methodDelete)


# Tenemos que actualizar la API a futuro