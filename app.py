# gcp debugger
try:
    import googleclouddebugger
    googleclouddebugger.enable(
            breakpoint_enable_canary=True
    )
except ImportError:
    pass

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import isrlCalc as isrlc


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/check-status")
def check_healt():
    return {"Status": "Active"}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
                        "index.html",
                        {"request": request})


@app.post("/handle-salary", response_class=HTMLResponse)
async def handle_salary(request: Request):
    errors = []
    resp = []
    result = []
    form_send = await request.form()
    if request.method == "POST":
        try:
            month_salary = float(form_send['salario'])
            afp_type = int(form_send['tipoAfp'])
            resp.append(month_salary)
            resp.append(afp_type)
        except request.NotSalaryFound:
            errors.append("No se pudo obtener el salario")

    if resp:
        result = isrlc.islr(resp[0], resp[1])
        result.append(resp[0])

    return templates.TemplateResponse(
                        "index.html",
                        {"request": request,
                         "result": result})
