from pydantic import BaseModel
from typing import Optional
from datetime import date


class PagoBase(BaseModel):
    oficina_id: int
    mes: int
    anio: int
    monto_pagado: float
    fecha_pago: Optional[date] = None
    observaciones: Optional[str] = None


class PagoCreate(PagoBase):
    pass


class PagoResponse(PagoBase):
    id: int

    class Config:
        from_attributes = True