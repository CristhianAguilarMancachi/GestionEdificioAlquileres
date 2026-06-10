from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.pago import Pago
from app.models.oficina import Oficina
from app.schemas.pago_schema import PagoCreate, PagoResponse

router = APIRouter(
    prefix="/pagos",
    tags=["Pagos"]
)


@router.post("/", response_model=PagoResponse)
def registrar_pago(pago: PagoCreate, db: Session = Depends(get_db)):
    oficina = db.query(Oficina).filter(Oficina.id == pago.oficina_id).first()

    if oficina is None:
        raise HTTPException(status_code=404, detail="Oficina no encontrada")

    pago_existente = db.query(Pago).filter(
        Pago.oficina_id == pago.oficina_id,
        Pago.mes == pago.mes,
        Pago.anio == pago.anio
    ).first()

    if pago_existente:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un pago registrado para esa oficina en ese mes y año"
        )

    nuevo_pago = Pago(**pago.model_dump())
    db.add(nuevo_pago)
    db.commit()
    db.refresh(nuevo_pago)

    return nuevo_pago


@router.get("/", response_model=list[PagoResponse])
def listar_pagos(db: Session = Depends(get_db)):
    return db.query(Pago).all()


@router.get("/oficina/{oficina_id}", response_model=list[PagoResponse])
def listar_pagos_por_oficina(oficina_id: int, db: Session = Depends(get_db)):
    oficina = db.query(Oficina).filter(Oficina.id == oficina_id).first()

    if oficina is None:
        raise HTTPException(status_code=404, detail="Oficina no encontrada")

    return db.query(Pago).filter(Pago.oficina_id == oficina_id).all()