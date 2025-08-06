from fastapi import APIRouter

from orders_service.app.config import settings

router = APIRouter(prefix=settings.api.orders, tags=['Orders'])


@router.post('/')
async def create_order():
    """Создание заказа."""
    pass


@router.get('/{id}')
async def get_order():
    """Получение заказа."""
    pass


@router.patch('/{id}')
async def update_order():
    """Изменение заказа."""
    pass


@router.delete('/{id}')
async def delete_order():
    """Удаление заказа."""
    pass
