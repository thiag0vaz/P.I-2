from sqlalchemy.orm import Session
from models.montadora_model import Montadora

def criar_montadora(db: Session, nome: str, pais: str, ano_fundacao: int) -> Montadora:
    montadora = Montadora(nome=nome, pais=pais, ano_fundacao=ano_fundacao)
    db.add(montadora)
    db.commit()
    db.refresh(montadora)
    return montadora

def listar_montadoras(db: Session):
    return db.query(Montadora).all()

def obter_montadora(db: Session, montadora_id: int) -> Montadora:
    return db.query(Montadora).filter(Montadora.id == montadora_id).first()

def editar_montadora(db: Session, montadora_id: int, nome: str, pais: str, ano_fundacao: int) -> Montadora:
    montadora = db.query(Montadora).filter(Montadora.id == montadora_id).first()
    if montadora:
        montadora.nome = nome
        montadora.pais = pais
        montadora.ano_fundacao = ano_fundacao
        db.commit()
        db.refresh(montadora)
    return montadora

def remover_montadora(db: Session, montadora_id: int) -> Montadora:
    montadora = db.query(Montadora).filter(Montadora.id == montadora_id).first()
    if montadora:
        db.delete(montadora)
        db.commit()
    return montadora
