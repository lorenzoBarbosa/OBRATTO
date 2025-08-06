from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.fornecedor import fornecedor_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/fornecedor/{id}")
async def get_fornecedor(request: Request, id: int):
    fornecedor = fornecedor_repo.obter_fornecedor_por_id(id)
    return templates.TemplateResponse("fornecedor.html", {"request": request, "fornecedor": fornecedor})