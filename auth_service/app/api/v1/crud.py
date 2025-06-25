from .schemas import CreateUser

def create_user(user: CreateUser) -> dict:
    """Создание пользователя."""
    user = user.model_dump()
    return {'success': True, 'user': user}