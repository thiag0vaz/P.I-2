from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Modelo(Base):
    __tablename__ = "modelos_veiculo"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    montadora_id = Column(Integer, ForeignKey('montadoras.id'))
    valor_referencia = Column(Float)
    motorizacao = Column(Float)
    turbo = Column(Boolean, default=False)
    automatico = Column(Boolean, default=False)

    montadora = relationship("Montadora", back_populates="modelos")
    veiculos = relationship("Veiculo", back_populates="modelo")