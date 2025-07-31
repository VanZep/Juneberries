from datetime import datetime

from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    """Схема создания пользователя."""

    id: int
    email: EmailStr
    password_hash: str
    name: str
    role_id: int
    created_at: datetime
