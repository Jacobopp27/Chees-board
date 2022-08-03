from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicial():
    return render_template('index.html', filas = 8, columnas = 8,  color1='white', color2 = 'green')

@app.route('/<val>')
def ocho_cualquiera(val):
    return render_template('index.html', filas = 8, columnas=int(val), color1='white', color2 = 'green')

@app.route('/<val1>/<val2>')
def cualquiera(val1, val2):
    return render_template('index.html', filas = int(val1), columnas=int(val2), color1='white', color2 = 'green')

@app.route('/<val1>/<val2>/<color1>/<color2>')
def cualquiera_color(val1, val2, color1, color2):
    return render_template('index.html', filas = int(val1), columnas=int(val2), color1=color1, color2 = color2)

if __name__ == '__main__':
    app.run(debug=True)
