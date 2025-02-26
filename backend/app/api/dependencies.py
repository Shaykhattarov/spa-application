from app.repositories.categories import ProductCategoryRepository
from app.repositories.units import ProductUnitRepository
from app.repositories.products import ProductRepository

from app.services.categories import ProductCategoryService
from app.services.units import ProductUnitService

from sqlmodel import Session
from app.core.database import engine


def get_session():
    with Session(engine) as session:
        yield session

product_category_repository = ProductCategoryRepository()
product_category_service = ProductCategoryService(product_category_repository)

product_unit_repository = ProductUnitRepository()
product_unit_service = ProductUnitService(product_unit_repository)
