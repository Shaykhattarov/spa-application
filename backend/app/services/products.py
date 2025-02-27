from app.repositories.products import ProductRepository
from fastapi import Depends


class ProductService:
    
    productRepository: ProductRepository

    def __init__(self, productRepository: ProductRepository = Depends()):
        self.productRepository = productRepository

    def create(self): ...

    def get(self): ...

    def patch(self): ...

    def delete(self): ...