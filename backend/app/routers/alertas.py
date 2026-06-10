from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.alertas_service import calcular_meses_adeudados

router = APIRouter(
    prefix="/alertas",
    tags=["Alertas"]
)


@router.get("/deudas")
def obtener_alertas_deudas(db: Session = Depends(get_db)):
    return calcular_meses_adeudados(db)