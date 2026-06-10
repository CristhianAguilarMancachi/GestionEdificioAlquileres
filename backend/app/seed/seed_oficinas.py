from sqlalchemy.orm import Session

from app.models.oficina import Oficina


def cargar_oficinas(db: Session):

    if db.query(Oficina).count() > 0:
        return

    oficinas = []

    # =====================
    # SUBSUELO
    # =====================

    for numero in range(1, 3):
        oficinas.append(
            Oficina(
                codigo=f"Subsuelo {numero}",
                piso="Subsuelo",
                monto_mensual=0,
                activa=True
            )
        )

    # =====================
    # PISO PRINCIPAL
    # =====================

    for numero in range(1, 11):
        oficinas.append(
            Oficina(
                codigo=str(numero),
                piso="Piso Principal",
                monto_mensual=0,
                activa=True
            )
        )

    # =====================
    # PISO 1
    # =====================

    for numero in range(101, 105):
        oficinas.append(
            Oficina(
                codigo=str(numero),
                piso="Piso 1",
                monto_mensual=0,
                activa=True
            )
        )

    # =====================
    # PISO 2
    # =====================

    for numero in range(201, 209):
        oficinas.append(
            Oficina(
                codigo=str(numero),
                piso="Piso 2",
                monto_mensual=0,
                activa=True
            )
        )

    db.add_all(oficinas)
    db.commit()