from fastapi import APIRouter

# controllers 
from controllers.methodGet import methodGet,methodGetId
from controllers.methodPost import methodPost
from controllers.methodPut import methodPut
from controllers.methodDelete import methodDelete

# Use multiple routers
router = APIRouter()


# routers of client
router.get("/banco")(methodGet)

router.get("/banco/{item_id}/saldo")(methodGetId)

router.post("/banco")(methodPost)

router.put("/banco/client/{item_id}")(methodPut)

router.delete("/banco/client/{item_id}")(methodDelete)

# routers of transaction





# Tenemos que actualizar la API a futuro