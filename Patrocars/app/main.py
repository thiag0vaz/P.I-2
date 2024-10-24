from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from controllers import montadora_controller, modelo_controller, veiculo_controller
from database import Base, engine
from core import templates

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(montadora_controller.router)
app.include_router(modelo_controller.router)
app.include_router(veiculo_controller.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
