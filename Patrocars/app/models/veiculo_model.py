from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base

class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    modelo_id = Column(Integer, ForeignKey('modelos_veiculo.id'))
    cor = Column(String)
    ano_fabricacao = Column(Integer)
    ano_modelo = Column(Integer)
    valor = Column(Float)
    placa = Column(String)
    vendido = Column(Boolean, default=False)

    modelo = relationship("Modelo", back_populates="veiculos")
