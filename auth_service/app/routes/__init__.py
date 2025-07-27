from fastapi import APIRouter

from config import settings
from .users import router as users_router

v1_router = APIRouter(prefix=settings.api.prefix)
v1_router.include_router(users_router, prefix=settings.api.v1)