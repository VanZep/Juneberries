from typing import Annotated

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from config import settings
from models import db_helper
from schemas.users import CreateUser
from crud.users import create_user

router = APIRouter(prefix=settings.api.auth, tags=['Auth'])


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter())],
        user: CreateUser
):
    """Регистрация пользователя."""
    return create_user(session, user)


@router.post('/login')
def login():
    """Логин пользователя."""
    pass


@router.get('/me')
def me():
    """Страница пользователя."""
    pass


@router.post('/refresh')
def refresh():
    """Обновление токена."""
    pass
