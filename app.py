import os
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET','POST'])
def index():
    errors = []
    result = []
    if request.method == 'POST':
        try:
            salario = float(request.form['salario'])
            tipoafp = int(request.form['tipoAfp'])
            print(f'Este es el salario ingresado {salario}')
            print(f'El tipo de afp es {tipoafp}')
            print(type(salario))
            print(type(tipoafp))
            result.append(salario)
            result.append(tipoafp)
        except:
            errors.append("No se pudo obtener el salario")
    return render_template('index.html',result=result)

if __name__ == '__main__':
    app.run(debug = True)
