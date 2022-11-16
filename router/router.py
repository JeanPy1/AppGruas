from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from model.db import select
from schema.worker import User


router = APIRouter()
templates = Jinja2Templates(directory="./templates")

@router.get("/", response_class=HTMLResponse, status_code=200)
async def index(request: Request):
    query = f"""SELECT * FROM WORKERS"""
    result = select(query)    
    data = []
    for worker in result:
        mydict = {  "dni": worker[0],
                    "nombre": worker[1]}
        data.append(mydict)

    return templates.TemplateResponse("index.html", {"request": request, "message": data})  
   



#@router.post("/user")
#def create_worker(worker: Worker):
#    query = f"""INSERT INTO WORKERS (DNI, NAME) VALUES ("{worker.dni}", "{worker.nombre}")"""
#    result = insert(query)
#    return result

@router.post("/user", response_class=HTMLResponse)
def create_worker(user: User):
    print(user)
    return {"hola": "jeancarlos"}