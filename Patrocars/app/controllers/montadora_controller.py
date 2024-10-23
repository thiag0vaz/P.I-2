from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from models.montadora_model import Montadora
from database import get_db
from core import templates

router = APIRouter()

@router.get("/montadoras/", response_class=HTMLResponse)
def listar_montadoras(request: Request, db: Session = Depends(get_db)):
    montadoras = db.query(Montadora).all()
    return templates.TemplateResponse("list_montadoras.html", {"request": request, "montadoras": montadoras})

@router.get("/montadoras/add", response_class=HTMLResponse)
def form_add_montadora(request: Request):
    return templates.TemplateResponse("add_montadora.html", {"request": request})

@router.post("/montadoras/add")
async def add_montadora(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    montadora = Montadora(nome=form["nome"], pais=form["pais"], ano_fundacao=int(form["ano_fundacao"]))
    db.add(montadora)
    db.commit()
    return RedirectResponse(url="/montadoras/", status_code=303)

@router.get("/montadoras/{montadora_id}/edit", response_class=HTMLResponse)
def form_edit_montadora(montadora_id: int, request: Request, db: Session = Depends(get_db)):
    montadora = db.query(Montadora).filter(Montadora.id == montadora_id).first()
    return templates.TemplateResponse("edit_montadora.html", {"request": request, "montadora": montadora})

@router.post("/montadoras/{montadora_id}/edit")
async def edit_montadora(montadora_id: int, request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    montadora = db.query(Montadora).filter(Montadora.id == montadora_id).first()
    montadora.nome = form["nome"]
    montadora.pais = form["pais"]
    montadora.ano_fundacao = int(form["ano_fundacao"])
    db.commit()
    return RedirectResponse(url="/montadoras/", status_code=303)

@router.get("/montadoras/{montadora_id}/delete")
def delete_montadora(montadora_id: int, db: Session = Depends(get_db)):
    montadora = db.query(Montadora).filter(Montadora.id == montadora_id).first()
    db.delete(montadora)
    db.commit()
    return RedirectResponse(url="/montadoras/", status_code=303)
