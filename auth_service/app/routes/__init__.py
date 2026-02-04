from fastapi import APIRouter

from config import settings
from .auth import router as auth_router

v1_router = APIRouter(prefix=settings.api.prefix)
v1_router.include_router(auth_router, prefix=settings.api.v1)
