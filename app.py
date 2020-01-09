import os
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET','POST'])
def index():
    errors = []
    
    if request.method == 'POST':
        try:
            salario = request.form['salario']
            print(f'Este es el salario ingresado {salario}')
        except:
            errors.append("No se pudo obtener el salario")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
