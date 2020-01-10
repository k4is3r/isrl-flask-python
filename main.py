import os
from flask import Flask, render_template, request, send_from_directory
import isrlCalc as isrlc

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET','POST'])
def index():
    errors = []
    resp = []
    result = [] 
    if request.method == 'POST':
        try:
            salario = float(request.form['salario'])
            tipoafp = int(request.form['tipoAfp'])
            resp.append(salario)
            resp.append(tipoafp)
        except:
            errors.append("No se pudo obtener el salario")
    
    if resp:
        result = isrlc.islr(resp[0],resp[1])
        result.append(resp[0])

    return render_template('index.html', result = result)


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080, debug = True)
