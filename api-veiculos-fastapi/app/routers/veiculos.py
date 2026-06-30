from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Veiculo, VeiculoCreate, VeiculoUpdate, VeiculoORM
router = APIRouter(prefix="/veiculos", tags=["Veículos"])
@router.get("/", response_model=list[Veiculo])
def listar_veiculos(db: Session = Depends(get_db)):
    return db.query(VeiculoORM).all()
@router.get("/{veiculo_id}", response_model=Veiculo)
def obter_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoORM).filter(VeiculoORM.id == veiculo_id).first()
    if not veiculo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Veículo não encontrado.")
    return veiculo
@router.post("/", response_model=Veiculo, status_code=status.HTTP_201_CREATED)
def criar_veiculo(dados: VeiculoCreate, db: Session = Depends(get_db)):
    novo_veiculo = VeiculoORM(**dados.model_dump())
    db.add(novo_veiculo)
    db.commit()
    db.refresh(novo_veiculo)
    return novo_veiculo
@router.put("/{veiculo_id}", response_model=Veiculo)
def atualizar_veiculo(veiculo_id: int, dados: VeiculoCreate, db: Session =
Depends(get_db)):
    veiculo = db.query(VeiculoORM).filter(VeiculoORM.id == veiculo_id).first()
    if not veiculo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Veículo não encontrado.")
    for campo, valor in dados.model_dump().items():
        setattr(veiculo, campo, valor)
    db.commit()
    db.refresh(veiculo)
    return veiculo
@router.patch("/{veiculo_id}", response_model=Veiculo)
def atualizar_parcial_veiculo(veiculo_id: int, dados: VeiculoUpdate, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoORM).filter(VeiculoORM.id == veiculo_id).first()
    if not veiculo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Veículo não encontrado.")
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(veiculo, campo, valor)
    db.commit()
    db.refresh(veiculo)
    return veiculo
@router.delete("/{veiculo_id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoORM).filter(VeiculoORM.id == veiculo_id).first()
    if not veiculo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Veículo não encontrado.")
    db.delete(veiculo)
    db.commit()
