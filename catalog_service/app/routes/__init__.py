from fastapi import APIRouter

from config import settings
from .products import router as products_router

v1_router = APIRouter(prefix=settings.api.prefix)
v1_router.include_router(products_router, prefix=settings.api.v1)