from fastapi import APIRouter
from app.models.products import Product



router = APIRouter(prefix='/products', tags=['product'])



@router.post('/', response_model=Product)
def create(): ...