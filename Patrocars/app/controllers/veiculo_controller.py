from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from models.veiculo_model import Veiculo
from models.modelo_model import Modelo
from models.montadora_model import Montadora
from database import get_db
from core import templates 

router = APIRouter()

@router.get("/veiculos/", response_class=HTMLResponse)
def listar_veiculos(request: Request, db: Session = Depends(get_db)):
    veiculos = db.query(Veiculo).all()
    return templates.TemplateResponse("list_veiculos.html", {"request": request, "veiculos": veiculos})

@router.get("/veiculos/add", response_class=HTMLResponse)
def form_add_veiculo(request: Request, db: Session = Depends(get_db)):
    montadoras = db.query(Montadora).all()
    return templates.TemplateResponse("add_veiculo.html", {"request": request, "montadoras": montadoras})

@router.post("/veiculos/add")
async def add_veiculo(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    veiculo = Veiculo(
        cor=form["cor"],
        ano_fabricacao=int(form["ano_fabricacao"]),
        ano_modelo=int(form["ano_modelo"]),
        valor=float(form["valor"]),
        placa=form["placa"],
        vendido=bool(form.get("vendido", False)),
        modelo_id=int(form["modelo_id"])
    )
    db.add(veiculo)
    db.commit()
    return RedirectResponse(url="/veiculos/", status_code=303)

@router.get("/veiculos/{veiculo_id}/edit", response_class=HTMLResponse)
def form_edit_veiculo(veiculo_id: int, request: Request, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    modelos = db.query(Modelo).all()
    return templates.TemplateResponse("edit_veiculo.html", {"request": request, "veiculo": veiculo, "modelos": modelos})

@router.post("/veiculos/{veiculo_id}/edit")
async def edit_veiculo(veiculo_id: int, request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    veiculo.cor = form["cor"]
    veiculo.ano_fabricacao = int(form["ano_fabricacao"])
    veiculo.ano_modelo = int(form["ano_modelo"])
    veiculo.valor = float(form["valor"])
    veiculo.placa = form["placa"]
    veiculo.vendido = bool(form.get("vendido", False))
    veiculo.modelo_id = int(form["modelo_id"])
    db.commit()
    return RedirectResponse(url="/veiculos/", status_code=303)

@router.get("/veiculos/{veiculo_id}/delete")
def delete_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    db.delete(veiculo)
    db.commit()
    return RedirectResponse(url="/veiculos/", status_code=303)
