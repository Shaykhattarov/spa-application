from fastapi import Depends, status
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from starlette.responses import Response, JSONResponse

from app.models.categories import ProductCategory
from app.repositories.categories import ProductCategoryRepository
from app.schemas.categories import ProductCategoryScheme



class ProductCategoryService:

    productCategoryRepository: ProductCategoryRepository

    def __init__(self, productCategoryRepository: ProductCategoryRepository = Depends()) -> None:
        self.productCategoryRepository = productCategoryRepository

    def create(self, productCategoryScheme: ProductCategoryScheme) -> Response:
        new_obj: ProductCategory | None = self.productCategoryRepository.create(ProductCategory(name=productCategoryScheme.name))
        if new_obj is not None:
            return Response(
                status_code=status.HTTP_201_CREATED, 
                headers={
                    "location": f"/{ProductCategory.__tablename__}/{new_obj.id}"
                }
            )
        else:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


    def get(self, id: int) -> ProductCategory:
        response = self.productCategoryRepository.get(
            ProductCategory(id=id)
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
    ) -> List[ProductCategory]:
        response: List[ProductCategory] = self.productCategoryRepository.page(skip, limit)
        content = {
            "skip": skip,
            "limit": limit,
            "count": len(response),
            "data": response
        }
        return JSONResponse(
            content=jsonable_encoder(content)
        )
