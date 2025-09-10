from tempfile import template
from fastapi import Request
from websockets import Router


@Router.get("/")
async def get_root(request: Request):    
    return template.TemplateResponse("publico/home.html", {"request": request})