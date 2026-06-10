from datetime import date
from sqlalchemy.orm import Session

from app.models.oficina import Oficina
from app.models.pago import Pago


def calcular_meses_adeudados(db: Session):
    fecha_actual = date.today()
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year

    oficinas = db.query(Oficina).all()
    alertas = []

    for oficina in oficinas:

        if not oficina.activa:
            continue

        meses_deuda = []

        for i in range(1, 4):
            mes = mes_actual - i
            anio = anio_actual

            if mes <= 0:
                mes += 12
                anio -= 1

            pago = db.query(Pago).filter(
                Pago.oficina_id == oficina.id,
                Pago.mes == mes,
                Pago.anio == anio
            ).first()

            if pago is None:
                meses_deuda.append({
                    "mes": mes,
                    "anio": anio
                })

        if len(meses_deuda) >= 2:
            alertas.append({
                "oficina_id": oficina.id,
                "codigo": oficina.codigo,
                "piso": oficina.piso,
                "monto_mensual": oficina.monto_mensual,
                "meses_adeudados": len(meses_deuda),
                "detalle_meses": meses_deuda,
                "deuda_estimada": oficina.monto_mensual * len(meses_deuda)
            })

    return alertas