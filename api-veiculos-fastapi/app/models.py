from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy import Column, Integer, String, Float
from database import Base
class VeiculoBase(BaseModel):
    placa: str = Field(..., min_length=7, max_length=8, examples=["ABC1D23"])
    marca: str = Field(..., min_length=2, max_length=50)
    modelo: str = Field(..., min_length=1, max_length=50)
    ano_fabricacao: int = Field(..., ge=1950, le=2026)
    cor: str = Field(..., max_length=30)
    quilometragem: float = Field(default=0.0, ge=0)
class VeiculoCreate(VeiculoBase):
    """Schema usado na criação (POST)."""
    pass
class VeiculoUpdate(BaseModel):
    """Schema usado na atualização parcial (PATCH) - todos os campos opcionais."""
    placa: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ano_fabricacao: Optional[int] = None
    cor: Optional[str] = None
    quilometragem: Optional[float] = None
class Veiculo(VeiculoBase):
    """Schema de resposta (inclui o identificador gerado pelo servidor)."""
    id: int
    class Config:
        from_attributes = True
class VeiculoORM(Base):
    __tablename__ = "veiculos"
    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(8), unique=True, nullable=False, index=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    ano_fabricacao = Column(Integer, nullable=False)
    cor = Column(String(30), nullable=False)
    quilometragem = Column(Float, default=0.0, nullable=False)