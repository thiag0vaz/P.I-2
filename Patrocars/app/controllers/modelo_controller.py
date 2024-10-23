from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from models.modelo_model import Modelo
from models.montadora_model import Montadora
from database import get_db
from core import templates
from typing import List
from pydantic import BaseModel

router = APIRouter()


class ModeloResponse(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True

@router.get("/modelos/", response_class=HTMLResponse)
def listar_modelos(request: Request, db: Session = Depends(get_db)):
    modelos = db.query(Modelo).all()
    return templates.TemplateResponse("list_modelos.html", {"request": request, "modelos": modelos})

@router.get("/modelos/add", response_class=HTMLResponse)
def form_add_modelo(request: Request, db: Session = Depends(get_db)):
    montadoras = db.query(Montadora).all()  # Para preencher o campo de seleção de montadoras
    return templates.TemplateResponse("add_modelo.html", {"request": request, "montadoras": montadoras})

@router.post("/modelos/add")
async def add_modelo(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    modelo = Modelo(
        nome=form["nome"],
        montadora_id=int(form["montadora_id"]),
        valor_referencia=float(form["valor_referencia"]),
        motorizacao=float(form["motorizacao"]),
        turbo=bool(form.get("turbo", False)),
        automatico=bool(form.get("automatico", False))
    )
    db.add(modelo)
    db.commit()
    return RedirectResponse(url="/modelos/", status_code=303)

@router.get("/modelos/{modelo_id}/edit", response_class=HTMLResponse)
def form_edit_modelo(modelo_id: int, request: Request, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    montadoras = db.query(Montadora).all()
    return templates.TemplateResponse("edit_modelo.html", {"request": request, "modelo": modelo, "montadoras": montadoras})

@router.post("/modelos/{modelo_id}/edit")
async def edit_modelo(modelo_id: int, request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    modelo = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    modelo.nome = form["nome"]
    modelo.montadora_id = int(form["montadora_id"])
    modelo.valor_referencia = float(form["valor_referencia"])
    modelo.motorizacao = float(form["motorizacao"])
    modelo.turbo = bool(form.get("turbo", False))
    modelo.automatico = bool(form.get("automatico", False))
    db.commit()
    return RedirectResponse(url="/modelos/", status_code=303)

@router.get("/modelos/{modelo_id}/delete")
def delete_modelo(modelo_id: int, db: Session = Depends(get_db)):
    modelo = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    db.delete(modelo)
    db.commit()
    return RedirectResponse(url="/modelos/", status_code=303)

@router.get("/modelos/montadora/{montadora_id}", response_model=List[ModeloResponse])
def listar_modelos_por_montadora(montadora_id: int, db: Session = Depends(get_db)):
    modelos = db.query(Modelo).filter(Modelo.montadora_id == montadora_id).all()
    return modelos  
