from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Montadora(Base):
    __tablename__ = "montadoras"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    pais = Column(String)
    ano_fundacao = Column(Integer)

    modelos = relationship("Modelo", back_populates="montadora")
