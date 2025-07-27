from fastapi import APIRouter

from config import settings


router = APIRouter(prefix=settings.api.products, tags=['Products'])

@router.get('/')
async def get_all_products():
    pass


@router.get('/{id}')
async def get_product(id: int):
    pass


@router.post('/')
async def create_product():
    pass


@router.put('/{id}')
async def update_product(id: int):
    pass


@router.delete('/{id}')
async def delete_product(id: int):
    pass