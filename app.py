from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional
import isrlCalc as isrlc

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/check-status")
def check_healt():
    return {"Status":"Active"}

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/handle-salary", response_class=HTMLResponse)
def handle_salary(request: Request):
    errors = []
    resp = []
    result = []
    if request.method == 'POST':
        try:
            month_salary = float(request.form['salario'])
            afp_type = int(request.form['tipoAfp'])
            resp.append(month_salary)
            resp.append(afp_type)
        except :
            errors.append("No se pudo obtener el salario")

    if resp:
        result = isrlc.islr(resp[0], resp[1])
        result.append(resp[0])

    return templates.TemplateResponse("index.html", {"request":request, "result":result})
