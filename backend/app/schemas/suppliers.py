from pydantic import BaseModel



class SupplierScheme(BaseModel):
    name: str
    category_id: int



class SupplierUpdateScheme(SupplierScheme):
    id: int