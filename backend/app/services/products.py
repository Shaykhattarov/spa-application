from typing import List
from fastapi import Depends, status
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse

from app.models.products import Product
from app.schemas.products import ProductScheme
from app.repositories.products import ProductRepository


class ProductService:
    
    productRepository: ProductRepository

    def __init__(self, productRepository: ProductRepository = Depends()):
        self.productRepository = productRepository

    def create(self, productScheme: ProductScheme) -> Response:
        response: Product | None = self.productRepository.create(
            Product(
                productScheme.name,
                productScheme.category_id,
                productScheme.unit_id,
                productScheme.retail_price
            )
        )

        if response is None:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
        return Response(
            status_code=status.HTTP_200_OK,
            headers={
                "location": f"/{Product.__tablename__}/{response.id}" 
            }
        )
        

    def get(self, id: int) -> Response | JSONResponse:
        response = self.productRepository.get(
            Product(id=id)
        )
        if response is None:
            return Response(
                status_code=status.HTTP_404_NOT_FOUND
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=jsonable_encoder(response)
            )
        
    def page(
            self,
            skip: int,
            limit: int
    ) -> JSONResponse:
        response: List[Product] = self.productRepository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response
        }
        return JSONResponse(
            content=jsonable_encoder(content)
        )

    def patch(self): ...

    def delete(self): ...