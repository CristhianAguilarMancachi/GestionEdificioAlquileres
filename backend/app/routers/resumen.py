from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.oficina import Oficina
from app.services.alertas_service import calcular_meses_adeudados

router = APIRouter(
    prefix="/resumen",
    tags=["Resumen"]
)


@router.get("/")
def obtener_resumen(db: Session = Depends(get_db)):

    oficinas_activas = db.query(Oficina).filter(
        Oficina.activa == True
    ).count()

    alertas = calcular_meses_adeudados(db)

    deuda_total = sum(
        alerta["deuda_estimada"]
        for alerta in alertas
    )

    return {
        "oficinas_activas": oficinas_activas,
        "oficinas_con_alerta": len(alertas),
        "deuda_total": deuda_total
    }