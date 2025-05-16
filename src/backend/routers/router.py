from fastapi import APIRouter

# controllers 
from controllers.methodGet import methodGet
from controllers.methodPost import methodPost
from controllers.methodPut import methodPut

# Use multiple routers
router = APIRouter()


# routers of client
router.get("/")(methodGet)

router.post("/")(methodPost)

router.put("/{item_id}")(methodPut)


# routers of transaction