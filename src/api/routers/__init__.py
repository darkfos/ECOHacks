from .user_router import user_router
from .report_router import report_router
from fastapi import APIRouter


v1_router: APIRouter = APIRouter(prefix="/v1", tags=["v1/api"])
v1_router.include_router(user_router)
v1_router.include_router(report_router)