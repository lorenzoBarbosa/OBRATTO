from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional, List
from config import templates

router = APIRouter()

# Rota para agenda do prestador
@router.get("/agenda")
async def agenda_prestador(request: Request):
    return templates.TemplateResponse("prestador/agenda.html", {"request": request})

