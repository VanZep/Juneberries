from fastapi import APIRouter

from config import settings

router = APIRouter(prefix=settings.api.products, tags=['Products'])


@router.get('/')
async def get_all_products():
    """Получение всех товаров."""
    pass


@router.get('/{id}')
async def get_product(id: int):
    """Получения товара по ID."""
    pass


@router.post('/')
async def create_product():
    """Создание товара."""
    pass


@router.put('/{id}')
async def update_product(id: int):
    """Изменение товара."""
    pass


@router.delete('/{id}')
async def delete_product(id: int):
    """Удаление товара."""
    pass
