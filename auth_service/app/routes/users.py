from fastapi import APIRouter

from config import settings
from schemas.users import CreateUser
from crud.users import create_user

router = APIRouter(prefix=settings.api.auth, tags=['Users'])


@router.post('/register')
def register(user: CreateUser):
    """Регистрация пользователя."""
    return create_user(user)


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
