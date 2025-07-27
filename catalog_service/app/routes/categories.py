from fastapi import APIRouter

from config import settings

router = APIRouter(prefix=settings.api.categories, tags=['Categories'])


@router.get('/')
async def get_all_categories():
    pass


@router.post('/')
async def create_category():
    pass


@router.put('/{id}')
async def update_category(id: int):
    pass


@router.delete('/{id}')
async def delete_category(id: int):
    pass
