from fastapi import FastAPI

from app.database import Base, engine, SessionLocal

from app.models.oficina import Oficina
from app.models.pago import Pago

from app.routers import oficinas, pagos, alertas
from app.routers import resumen

from app.seed.seed_oficinas import cargar_oficinas


Base.metadata.create_all(bind=engine)


db = SessionLocal()
cargar_oficinas(db)
db.close()


app = FastAPI(
    title="Gestión de Edificio y Alquileres",
    version="1.0.0"
)

app.include_router(oficinas.router)
app.include_router(pagos.router)
app.include_router(alertas.router)
app.include_router(resumen.router)


@app.get("/")
def inicio():
    return {
        "mensaje": "Backend funcionando correctamente"
    }