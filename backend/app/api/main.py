from fastapi import APIRouter
from app.api.routing import categories
from app.api.routing import products
from app.api.routing import units
from app.api.routing import suppliers
from app.api.routing import supplies
from app.api.routing import supply_items
from app.api.routing import supply_surcharges
from app.api.routing import stores
from app.api.routing import addresses
from app.api.routing import store_schedules
from app.api.routing import employees
from app.api.routing import employee_positions
from app.api.routing import administrators



api_router = APIRouter()

api_router.include_router(products.router)
api_router.include_router(suppliers.router)
api_router.include_router(supplies.router)
api_router.include_router(supply_items.router)
api_router.include_router(supply_surcharges.router)
api_router.include_router(stores.router)
api_router.include_router(addresses.router)
api_router.include_router(store_schedules.router)
api_router.include_router(employees.router)
api_router.include_router(employee_positions.router)
api_router.include_router(administrators.router)
api_router.include_router(categories.router)
api_router.include_router(units.router)
# if settings.ENVIRONMENT == "local":
#    api_router.include_router(test.router)
