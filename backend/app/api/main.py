from fastapi import APIRouter
from app.api.routing import categories
from app.api.routing import products
from app.api.routing import units
from app.api.routing import suppliers
from app.api.routing import supplies
from app.api.routing import supply_items
from app.api.routing import supply_surcharges

from app.core.config import settings


api_router = APIRouter()
api_router.include_router(categories.router)
api_router.include_router(products.router)
api_router.include_router(units.router)
api_router.include_router(suppliers.router)
api_router.include_router(supplies.router)
api_router.include_router(supply_items.router)
api_router.include_router(supply_surcharges.router)

# if settings.ENVIRONMENT == "local":
#    api_router.include_router(test.router)