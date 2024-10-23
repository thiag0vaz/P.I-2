from sqlalchemy.orm import Session
from models.veiculo_model import Veiculo

def criar_veiculo(db: Session, cor: str, ano_fabricacao: int, ano_modelo: int, valor: float, placa: str, vendido: bool, modelo_id: int) -> Veiculo:
    veiculo = Veiculo(
        cor=cor,
        ano_fabricacao=ano_fabricacao,
        ano_modelo=ano_modelo,
        valor=valor,
        placa=placa,
        vendido=vendido,
        modelo_id=modelo_id
    )
    db.add(veiculo)
    db.commit()
    db.refresh(veiculo)
    return veiculo

def listar_veiculos(db: Session):
    return db.query(Veiculo).all()

def obter_veiculo(db: Session, veiculo_id: int) -> Veiculo:
    return db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()

def editar_veiculo(db: Session, veiculo_id: int, cor: str, ano_fabricacao: int, ano_modelo: int, valor: float, placa: str, vendido: bool, modelo_id: int) -> Veiculo:
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo:
        veiculo.cor = cor
        veiculo.ano_fabricacao = ano_fabricacao
        veiculo.ano_modelo = ano_modelo
        veiculo.valor = valor
        veiculo.placa = placa
        veiculo.vendido = vendido
        veiculo.modelo_id = modelo_id
        db.commit()
        db.refresh(veiculo)
    return veiculo

def remover_veiculo(db: Session, veiculo_id: int) -> Veiculo:
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo:
        db.delete(veiculo)
        db.commit()
    return veiculo
