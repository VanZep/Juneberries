from fastapi import APIRouter

from .users import router as users_router

v1_users_router = APIRouter(prefix='/v1')
v1_users_router.include_router(users_router)