from fastapi import FastAPI
from routers import veiculos
from database import Base, engine
app = FastAPI(
    title="API de Veículos",
    description="API construída na disciplina de PABD - TADS/IFRN",
    version="1.0.0",
)

app.include_router(veiculos.router)

@app.get("/")
def read_root():
 return {"mensagem": "API de Veículos no ar!"}

Base.metadata.create_all(bind=engine)