from pydantic import BaseModel
from typing import Optional


class OficinaBase(BaseModel):
    codigo: str
    piso: str
    monto_mensual: float
    observaciones: Optional[str] = None
    activa: bool = True


class OficinaCreate(OficinaBase):
    pass


class OficinaResponse(OficinaBase):
    id: int

    class Config:
        from_attributes = True