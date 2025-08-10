from fastapi import APIRouter

from config import settings
from .orders import router

v1_router = APIRouter(prefix=settings.api.prefix)
v1_router.include_router(router, prefix=settings.api.v1)
