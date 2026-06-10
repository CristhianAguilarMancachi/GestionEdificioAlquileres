from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship

from app.database import Base


class Oficina(Base):
    __tablename__ = "oficinas"

    id = Column(Integer, primary_key=True, index=True)

    codigo = Column(String, unique=True, nullable=False)

    piso = Column(String, nullable=False)

    monto_mensual = Column(Float, nullable=False)

    observaciones = Column(String, nullable=True)

    activa = Column(Boolean, default=True)

    pagos = relationship(
        "Pago",
        back_populates="oficina",
        cascade="all, delete"
    )