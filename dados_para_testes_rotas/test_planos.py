"""
Arquivo principal para testar as rotas de planos
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.fornecedor.fornecedor_planos import router as planos_router

app = FastAPI(title="OBRATTO - Test Planos")

# Configurar templates
templates = Jinja2Templates(directory="templates")

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Incluir as rotas de planos
app.include_router(planos_router, prefix="/fornecedor/planos", tags=["planos"])

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("test_index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
