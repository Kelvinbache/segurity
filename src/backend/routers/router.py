from fastapi import APIRouter, Request

# controllers 
from controllers.methodGet import methodGet,methodGetId

from controllers.methodPost import methodPost

from controllers.methodPatch import methodPatch

from controllers.methodDelete import methodDelete

# Model 
# from model.Models import (User)

# Use multiple routers
router = APIRouter( prefix="/v1", tags=["v1"],)

# show balance
router.get("/banco")(methodGet)

# show the details
router.get("/banco/saldo/{rol_user}/{item_id}", name="home")(methodGetId)

# check if the client exists
router.post("/banco")(methodPost)

# Update the list of contact
router.put("/banco/client/{item_id}")(methodPatch)

router.delete("/banco/client/{item_id}")(methodDelete)


# Tenemos que actualizar la API a futuro