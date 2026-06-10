from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.oficina import Oficina
from app.schemas.oficina_schema import OficinaCreate, OficinaResponse

router = APIRouter(
    prefix="/oficinas",
    tags=["Oficinas"]
)

@router.post("/", response_model=OficinaResponse)
def crear_oficina(oficina: OficinaCreate, db: Session = Depends(get_db)):
    nueva_oficina = Oficina(**oficina.model_dump())
    db.add(nueva_oficina)
    db.commit()
    db.refresh(nueva_oficina)
    return nueva_oficina

@router.get("/", response_model=list[OficinaResponse])
def listar_oficinas(db: Session = Depends(get_db)):
    return db.query(Oficina).all()

@router.put("/{oficina_id}", response_model=OficinaResponse)
def actualizar_oficina(
    oficina_id: int,
    oficina_actualizada: OficinaCreate,
    db: Session = Depends(get_db)
):
    oficina = db.query(Oficina).filter(Oficina.id == oficina_id).first()

    if oficina is None:
        return {"error": "Oficina no encontrada"}

    oficina.codigo = oficina_actualizada.codigo
    oficina.piso = oficina_actualizada.piso
    oficina.monto_mensual = oficina_actualizada.monto_mensual
    oficina.observaciones = oficina_actualizada.observaciones
    oficina.activa = oficina_actualizada.activa

    db.commit()
    db.refresh(oficina)

    return oficina


@router.delete("/{oficina_id}")
def eliminar_oficina(oficina_id: int, db: Session = Depends(get_db)):
    oficina = db.query(Oficina).filter(Oficina.id == oficina_id).first()

    if oficina is None:
        return {"error": "Oficina no encontrada"}

    db.delete(oficina)
    db.commit()

    return {"mensaje": "Oficina eliminada correctamente"}

@router.get("/{oficina_id}", response_model=OficinaResponse)
def obtener_oficina(
    oficina_id: int,
    db: Session = Depends(get_db)
):
    oficina = db.query(Oficina).filter(
        Oficina.id == oficina_id
    ).first()

    if oficina is None:
        raise HTTPException(
            status_code=404,
            detail="Oficina no encontrada"
        )

    return oficina