from fastapi import Depends, status
from typing import Annotated, Optional, List
from starlette.responses import Response, JSONResponse

from app.models.suppliers import Supplier
from app.schemas.suppliers import SupplierScheme
from app.repositories.suppliers import SupplierRepository




class SupplierService:

    supplierRepository: SupplierRepository

    def __init__(self, supplierRepository: SupplierRepository = Depends()):
        self.supplierRepository = supplierRepository

    def create(self, supplierScheme: SupplierScheme) -> Response:
        response: Optional[Supplier] = self.supplierRepository.create(
            Supplier(
                name=supplierScheme.name, 
                category_id=supplierScheme.category_id
            )
        )

        if response is None:
            return Response(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={
                "location": f"/{Supplier.__tablename__}/{response.id}"
            }
        )