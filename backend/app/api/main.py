from fastapi import APIRouter
from app.api.routing import categories
from app.api.routing import products
from app.api.routing import units

from app.core.config import settings


api_router = APIRouter()
api_router.include_router(categories.router)
api_router.include_router(products.router)
api_router.include_router(units.router)

# if settings.ENVIRONMENT == "local":
#    api_router.include_router(test.router)