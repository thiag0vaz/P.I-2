from sqlalchemy.orm import Session
from models.modelo_model import Modelo

def criar_modelo(db: Session, nome: str, montadora_id: int, valor_referencia: float, motorizacao: float, turbo: bool, automatico: bool) -> Modelo:
    modelo = Modelo(
        nome=nome,
        montadora_id=montadora_id,
        valor_referencia=valor_referencia,
        motorizacao=motorizacao,
        turbo=turbo,
        automatico=automatico
    )
    db.add(modelo)
    db.commit()
    db.refresh(modelo)
    return modelo

def listar_modelos(db: Session):
    return db.query(Modelo).all()

def obter_modelo(db: Session, modelo_id: int) -> Modelo:
    return db.query(Modelo).filter(Modelo.id == modelo_id).first()

def editar_modelo(db: Session, modelo_id: int, nome: str, montadora_id: int, valor_referencia: float, motorizacao: float, turbo: bool, automatico: bool) -> Modelo:
    modelo = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    if modelo:
        modelo.nome = nome
        modelo.montadora_id = montadora_id
        modelo.valor_referencia = valor_referencia
        modelo.motorizacao = motorizacao
        modelo.turbo = turbo
        modelo.automatico = automatico
        db.commit()
        db.refresh(modelo)
    return modelo

def remover_modelo(db: Session, modelo_id: int) -> Modelo:
    modelo = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    if modelo:
        db.delete(modelo)
        db.commit()
    return modelo
