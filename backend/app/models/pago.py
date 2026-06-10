from sqlalchemy import (
    Column,
    Integer,
    Float,
    Date,
    ForeignKey,
    String
)
from sqlalchemy.orm import relationship

from app.database import Base


class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)

    oficina_id = Column(
        Integer,
        ForeignKey("oficinas.id"),
        nullable=False
    )

    mes = Column(Integer, nullable=False)
    anio = Column(Integer, nullable=False)

    monto_pagado = Column(Float, nullable=False)

    fecha_pago = Column(Date, nullable=True)

    observaciones = Column(String, nullable=True)

    oficina = relationship(
        "Oficina",
        back_populates="pagos"
    )